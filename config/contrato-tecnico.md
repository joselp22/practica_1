# Contrato técnico común

Este archivo debe quedar **idéntico** en las tres ramas del experimento antes de que Kiro actúe.

- Lenguaje: **Python 3.11+**
- Framework API: **FastAPI**
- Pruebas: **pytest** y TestClient de FastAPI si se necesita
- Dependencias administradas en `requirements.txt`
- Aplicación en `src/main.py` con objeto `app` de FastAPI
- Pruebas en `tests/`
- Ejecución de pruebas esperada: `python -m pytest -q`
- No cambiar la HU o este contrato durante la fase de generación

**Variables de control:** mismo commit inicial, historia, sistema operativo, versión de Kiro, modelo elegido (si es configurable), configuración de permisos, tiempo disponible y criterio humano de evaluación. Usar sesiones nuevas y registrar incidencias.
