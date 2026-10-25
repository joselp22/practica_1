#!/usr/bin/env python3
"""Analiza el CSV del ejercicio T1 sin inventar puntuaciones ni resultados."""
from __future__ import annotations
import csv
from pathlib import Path
from html import escape
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "datos" / "resultados.csv"
OUT = ROOT / "resultados"
DIMS = ["fidelidad", "completitud", "verificabilidad", "seguridad", "trazabilidad"]


def numeric(row: dict, key: str, integer=False):
    value = (row.get(key) or "").strip()
    if not value:
        return None
    try:
        number = int(value) if integer else float(value)
    except ValueError as ex:
        raise ValueError(f"{row.get('ensayo','?')} | {key}: dato inválido {value!r}") from ex
    if integer and (number < 0 or (key in DIMS and number > 4)):
        raise ValueError(f"{row.get('ensayo','?')} | {key}: fuera de rango")
    if not integer and number < 0:
        raise ValueError(f"{row.get('ensayo','?')} | {key}: no puede ser negativo")
    return number


def main():
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        records = list(csv.DictReader(handle))
    summary = []
    for record in records:
        scores = [numeric(record, k, integer=True) for k in DIMS]
        quality = round(sum(scores) / 20 * 100, 1) if all(v is not None for v in scores) else None
        inventions = numeric(record, "invenciones", integer=True)
        ok = numeric(record, "pruebas_ok", integer=True)
        total = numeric(record, "pruebas_total", integer=True)
        if ok is not None and total is not None and ok > total:
            raise ValueError(f"{record.get('ensayo','?')}: pruebas_ok > pruebas_total")
        rate = round(ok / total * 100, 1) if ok is not None and total not in (None, 0) else None
        time = numeric(record, "tiempo_min")
        summary.append((record, quality, inventions, rate, time))

    def show(v, suffix=""):
        return f"{v}{suffix}" if v is not None else "Sin dato"

    lines = [
        "# Informe T1 — Resultados observados",
        "",
        "**Advertencia:** este informe usa únicamente las mediciones ingresadas por el evaluador. Los campos vacíos no representan ceros.",
        "",
        "| Ensayo | Prompt | Calidad (0–100) | Invenciones | Pruebas aprobadas (%) | Tiempo (min) |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for record, quality, inv, rate, tm in summary:
        lines.append(f"| {record['ensayo']} | {record['prompt']} | {show(quality)} | {show(inv)} | {show(rate, '%')} | {show(tm)} |")
    completed = [(rec, q, inv) for rec, q, inv, _, _ in summary if q is not None]
    lines += ["", "## Lectura del experimento", ""]
    if completed:
        by_quality = sorted(completed, key=lambda item: item[1], reverse=True)
        best = by_quality[0]
        lines.append(f"- El mayor puntaje de calidad registrado es **{best[1]} / 100** en **{best[0]['ensayo']}**. No implica por sí solo causalidad ni significancia estadística.")
        if len(completed) < 3:
            lines.append("- **Evaluación incompleta:** faltan puntuaciones en uno o más ensayos.")
        else:
            lines.append(f"- Calidad media de los tres ensayos: **{mean(item[1] for item in completed):.1f} / 100**.")
    else:
        lines.append("- **Aún no hay puntuaciones completas.** Ejecuta los ensayos y completa la rúbrica antes de afirmar cuál prompt obtuvo mejores resultados.")
    lines += [
        "- Las **invenciones** se contabilizan por separado para no ocultar riesgos detrás de la media.",
        "- Comprueba cada valor y evidencia con `evaluacion/checklist_revision_humana.md`.",
        "- Si el modelo o entorno cambió entre ensayos, incluye esa limitación en tus conclusiones.",
        "", "## Referencias a evidencia", "",
    ]
    for rec, *_ in summary:
        lines.append(f"- **{rec['ensayo']}** — commit: `{rec.get('commit') or 'pendiente'}`; evidencia: {rec.get('evidencia') or 'pendiente'}; evaluador: {rec.get('revisor') or 'pendiente'}.")
    OUT.mkdir(exist_ok=True)
    (OUT / "informe.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    if completed:
        width, height = 920, 420
        start_x, chart_top, chart_h, spacing = 130, 64, 275, 195
        rects=[]
        for idx, (record, quality, _) in enumerate(completed):
            x=start_x+idx*spacing
            h=chart_h*quality/100
            y=chart_top+chart_h-h
            rects.append(f'<rect x="{x}" y="{y:.1f}" width="116" height="{h:.1f}" rx="4" fill="#2563eb"/>')
            rects.append(f'<text x="{x+58}" y="{max(y-12,33):.1f}" text-anchor="middle" fill="#0f172a" font-size="17">{quality}%</text>')
            rects.append(f'<text x="{x+58}" y="{chart_top+chart_h+30}" text-anchor="middle" fill="#0f172a" font-size="16">{escape(record["ensayo"])}</text>')
        svg=f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="{width}" height="{height}" fill="#ffffff"/>
<text x="40" y="29" font-family="Arial" font-size="21" font-weight="bold" fill="#0f172a">Comparación T1: calidad verificada (%)</text>
<text x="40" y="53" font-family="Arial" font-size="12" fill="#64748b">Datos completos registrados manualmente; sin imputar valores ausentes</text>
<line x1="55" x2="870" y1="{chart_top+chart_h}" y2="{chart_top+chart_h}" stroke="#94a3b8"/>
{''.join(rects)}
</svg>"""
        (OUT / "comparacion.svg").write_text(svg, encoding="utf-8")
    print("Listo: resultados/informe.md" + (" y resultados/comparacion.svg" if completed else " (sin gráfico hasta tener puntuaciones completas)"))

if __name__ == "__main__":
    main()
