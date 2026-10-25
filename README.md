# Laboratorio T1: Kiro con control humano

**Objetivo:** comparar tres prompts sobre la misma historia de usuario (HU-001) para determinar cuándo la IA mejora el desarrollo y cuándo introduce riesgo.

**Principio:** la IA propone; una persona verifica y aprueba. No se atribuyen resultados que no hayan sido observados.

## Archivos principales

- `hu/HU-001.md`: requisito funcional fijo, idéntico para los tres experimentos.
- `config/contrato-tecnico.md`: stack, reglas y alcance compartidos.
- `prompts/`: tres prompts (mínimo, contextualizado y controlado).
- `evaluacion/`: rúbrica de puntuación y checklist de aprobación humana.
- `datos/resultados.csv`: formato vacío, sin valores inventados.
- `plantillas/Plantilla_Resultados_T1_Kiro.xlsx`: Excel alternativo para capturar notas y ver comparaciones. Si trabajas también con el informe automatizado, transcribe las mediciones al CSV.
- `scripts/analizar_resultados.py`: calcula comparaciones y genera informe real.
- `INSTRUCCIONES.md`: pasos para ejecutar en Kiro y Git.

**Técnicas:** Git para trazar versiones, Kiro para generar propuestas, pytest para ejecutar pruebas, CSV y script para analizar resultados.

### Paso rápido

1. Consulta `INSTRUCCIONES.md` y prepara un repositorio Git nuevo.
2. Registra el hash del commit base **antes** de experimentar.
3. Ejecuta cada prompt en su propia rama y en una conversación nueva de Kiro.
4. Conserva respuestas y logs; califica con las mismas reglas.
5. Completa las filas de `datos/resultados.csv` en la rama `base` al terminar los tres ensayos.
6. Ejecuta `python scripts/analizar_resultados.py` para generar `resultados/informe.md` y (si hay datos) `resultados/comparacion.svg`.

La carpeta `src/` empieza vacía a propósito. Su implementación es parte de lo que se medirá.
# practica_1
