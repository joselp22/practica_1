# Cómo llenar resultados.csv

Se incluyen tres filas **sin puntuar**. Completa las columnas numéricas solo con medidas reales:

- `fidelidad,completitud,verificabilidad,seguridad,trazabilidad`: números enteros de 0 a 4 según la rúbrica.
- `invenciones`: cantidad entera de añadidos no autorizados (0, 1, 2...).
- `pruebas_ok,pruebas_total`: cantidad real de pruebas ejecutadas/aprobadas. Si ninguna se pudo ejecutar, anota pruebas_total=0 y explica en la evidencia.
- `tiempo_min`: minutos observados, puede ser decimal.
- `commit`: hash del commit final de esa rama.
- `revisor`: quién calificó (iniciales o identificador no sensible).
- `evidencia`: nombre de archivo/captura o enlace verificable.

No uses `0` para indicar que **no mediste** algo. Deja la celda vacía. Tras llenar los datos, ejecuta `python scripts/analizar_resultados.py`.
