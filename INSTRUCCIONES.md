# Guía paso a paso — experimento en Kiro con Git

## Preparación del repositorio

1. Extrae el ZIP en una carpeta nueva y ábrela en Kiro.
2. Abre una terminal en esa carpeta.
3. Ejecuta:

```bash
git init -b base
git add .
git commit -m "Base fija del experimento T1 HU-001"
git rev-parse HEAD
```

4. Copia el hash mostrado en un lugar seguro (`BASE_SHA`). Es **el mismo punto de partida** de P1, P2 y P3.
5. Puedes crear un repositorio vacío en GitHub o GitLab y conectarlo con `git remote add origin URL_DEL_REPOSITORIO`. No publiques credenciales ni datos personales.

## Ensayo 1: mínimo

```bash
git switch -c experimento/p1-minimo BASE_SHA
```

Sustituye `BASE_SHA` por el hash real (sin escribir la palabra literal). Abre **una sesión nueva de Kiro**, pega exactamente `prompts/P1_minimo.txt`, registra su salida y deja que implemente la HU. No realices correcciones humanas mientras comparas la primera respuesta. Ejecuta las mismas comprobaciones de la rúbrica y guarda logs.

```bash
python -m pytest -q
git add .
git commit -m "P1 implementacion generada por Kiro"
git rev-parse HEAD
```

Si las pruebas fallan, registra el fallo; **no lo borres** para simular éxito.

## Ensayo 2: contextualizado

```bash
git switch -c experimento/p2-contexto BASE_SHA
```

En nueva sesión, pega `prompts/P2_contextualizado.txt`. Usa exactamente el mismo procedimiento de pruebas, captura, revisión y commit que P1.

## Ensayo 3: controlado

```bash
git switch -c experimento/p3-controlado BASE_SHA
```

En nueva sesión, pega `prompts/P3_controlado.txt`. Registra checkpoints de revisión, decisiones del humano y cualquier cambio aceptado antes de ejecutar. Si se pide autorización para alterar el alcance, no la concedas sin documentarlo. Igual que antes, realiza pruebas, revisión y commit.

## Registro y análisis central

Tras completar los tres ensayos, cambia a la rama original:

```bash
git switch base
```

Completa `datos/resultados.csv` con **valores observados** y el hash de cada rama. También puedes utilizar `plantillas/Plantilla_Resultados_T1_Kiro.xlsx` para visualizar las puntuaciones; los datos del Excel no se sincronizan automáticamente con el CSV. Ejecuta:

```bash
python scripts/analizar_resultados.py
```

El informe aparecerá en `resultados/informe.md`. El gráfico SVG aparecerá cuando exista al menos un ensayo con puntuaciones completas.

```bash
git add datos/resultados.csv resultados/
git commit -m "Registrar evaluaciones y resultados T1"
```

## Subida remota opcional

```bash
git push -u origin base
git push origin experimento/p1-minimo experimento/p2-contexto experimento/p3-controlado
```

## Principios para una comparación justa

- Una sola variable principal: el contenido del prompt. No cambies simultáneamente versión de Kiro, modelo, HU, entorno ni criterios.
- Si Kiro no puede controlar el modelo exactamente, documéntalo como limitación.
- Si Kiro propone detalles no definidos, anota la decisión; no cambies la HU a posteriori.
- No atribuyas las mejoras al prompt sin reconocer la variabilidad de las salidas de IA; tres corridas (una por tipo) sirven como **exploración inicial**, no prueba estadística definitiva.
- Para mayor confianza, repite tres veces cada prompt (9 ejecuciones), siempre desde el mismo commit base, antes de sacar conclusiones generales.

## Entregables del taller

1. Capturas o transcripciones de los tres prompts y respuestas.
2. Tres commits/rama con código y evidencia de pruebas.
3. Rúbrica y checklist llenados por persona.
4. Tabla de comparaciones, gráfico e informe.
5. Conclusión: ¿cuál prompt mejora el trabajo y bajo qué riesgos/limitaciones?
