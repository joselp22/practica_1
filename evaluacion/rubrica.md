# Rúbrica T1 (0–4 puntos por dimensión favorable)

Calificar **basándose en evidencia**, no en lo convincente del texto de Kiro.

| Dimensión | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Fidelidad | No respeta la HU | Respeta 1 CA | Respeta 2–3 CA | Respeta 4 CA | Respeta 5 CA |
| Completitud | Sin solución útil | Código incompleto | Implementa partes críticas | Funcional con detalles faltantes | Solución completa dentro del alcance |
| Verificabilidad | Sin pruebas ni instrucciones | Pruebas vagas/no reproducibles | Casos parciales | Pruebas reproducibles con omisiones | Casos CA-05 y resultados reproducibles |
| Seguridad | Acepta entradas inválidas | Controles casi ausentes | Valida algunas entradas | Valida entradas principales | Valida límites y no almacena entradas rechazadas |
| Trazabilidad | Sin vínculo con HU | Vínculos muy vagos | Algunos CA vinculados | Casi todos los CA trazados | Mapeo CA→archivo→prueba verificable |

**Invenciones:** número de elementos añadidos sin respaldo explícito en HU-001 o contrato técnico (por ejemplo: login, base de datos, etiquetas, fechas límite, servicio externo). Es un conteo aparte, no una calificación: 0 es ideal.

**Calidad total:** `(fidelidad + completitud + verificabilidad + seguridad + trazabilidad) / 20 * 100`.

- La calidad NO incluye directamente invenciones: se reportan aparte para que no se oculten dentro del promedio.
- `pruebas_ok` y `pruebas_total`: únicamente pruebas ejecutadas, no las que Kiro declara haber escrito.
- `tiempo_min`: minutos reales de principio a fin (cronómetro), con el mismo criterio en todos los ensayos.
- `evidencia`: ruta a log, archivo de capturas o URL del commit.

**Aprobación humana final:** solo si los 5 CA están implementados, no hay invenciones sin aprobar, pruebas relevantes pasan y no quedan riesgos críticos abiertos. Una buena nota no sustituye la aprobación humana.
