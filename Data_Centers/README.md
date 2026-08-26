# Data Centers · Costo ambiental de la infraestructura de la IA

Investigación abierta sobre el consumo de agua, energía y emisiones de CO₂ de los data centers a escala global.

**Investigación completa:** https://dempathyproject.com/investigaciones/datacenters/

---

## El problema

Menos del 1% de los data centers del mundo publica datos completos sobre su consumo eléctrico y de agua. Sin esa información no hay forma de medir el impacto sobre una comunidad, sobre su cuenca hidrológica, ni sobre las emisiones que genera.

Este repositorio contiene el dataset reconstruido, el diccionario de variables y el código de análisis. La idea es simple: si la industria no abre sus datos, que al menos el método para estimarlos sea público y auditable.

---

## El dataset

`datos/dc_trabajo.csv` — 5.314 data centers verificados · 147 países · 2.369 operadores

| Estado | Cantidad |
|---|---|
| Operativos | 5.263 |
| Planificados | 27 |
| En construcción | 24 |

**Fuentes:**

- **PeeringDB** (API `/api/fac`) — base de los registros operativos (~99% del dataset)
- **WRI Aqueduct 4.0** — riesgo hídrico por subcuenca, incorporado vía cruce espacial punto-en-polígono
- **Prensa especializada** (DataCenterKnowledge, DCD, Reuters, BlackRidge Research, Arizton) — megaproyectos con capacidad declarada

La columna `fuente_dato` registra la procedencia de cada fila.

El diccionario completo está en `datos/diccionario_variables.csv`: tipo, unidad, naturaleza (declarado / derivado / externo), fórmula de origen y rango de valores para cada columna.

---

## Fórmulas de estimación

Como la mayoría de las instalaciones no declara consumo, se estima a partir de la capacidad instalada mediante una cascada documentada.

**Consumo eléctrico**

```
C_elec = cap_mw_base × PUE × ρ
```

PUE = 1,58 (Lawrence Berkeley National Laboratory, 2024)
ρ = 0,70 — factor de ocupación (Uptime Institute, 2024)

**Huella hídrica**

```
W_directa   = C_elec × 1000 × WUE × 8760
W_indirecta = C_elec × 1000 × h_ind × 8760
W_total     = W_directa + W_indirecta
```

WUE = 1,8 L/kWh (Uptime Institute, 2024)
h_ind = WUE × 1,4 = 2,52 L/kWh — proxy de agua asociada a la generación eléctrica

**Emisiones**

```
E_CO2 = C_elec × FE_global × 8760
```

FE_global = 0,432 tCO₂/MWh (IEA, 2024)

**Capacidad base.** Para los 31 data centers con `cap_mw` declarada se usa el valor real. Para el resto se estima según `tamaño_porredes`:

| `tamaño_porredes` | Criterio | Capacidad de referencia |
|---|---|---|
| `local` | < 5 redes | 0,25 MW |
| `regional` | 5 – 19 redes | 3,0 MW |
| `nacional` | 20 – 99 redes | 20,0 MW |
| `internacional` | ≥ 100 redes | 100,0 MW |

---

## Limitaciones metodológicas

Explicitarlas es parte del método:

- **Colinealidad perfecta.** `agua_total_ml_año`, `consumo_electrico_mw` y `co2_ton_año` derivan de la misma estimación eléctrica base (Spearman ρ = 1,00 entre ellas). No pueden tratarse como dimensiones analíticas independientes.
- **`cap_mw` solo cubre 31 registros** (0,5% del dataset). El resto usa capacidad estimada por conectividad de red, que mide alcance de red y no potencia física.
- **La lista de proyectos en construcción no es un censo.** Es una selección de los megaproyectos con cobertura de prensa, así que sobrerrepresenta la escala grande.
- **Factor de emisión global.** Se usa el promedio IEA por ausencia de factores país por país, lo que subestima emisiones en matrices intensivas en carbón y las sobreestima en matrices limpias.
- **Unidades de agua.** Las columnas con sufijo `_ml_año` están en **litros por año**, no en millones de litros. El sufijo es histórico y quedó desactualizado.
- **`pue_estimado` y `wue_estimado`** son columnas heredadas cuyo método de cálculo no quedó documentado. No intervienen en ninguna fórmula publicada. Tratar con cautela.

---

## Estructura

```
Data_Centers/
├── datos/
│   ├── dc_trabajo.csv               # dataset principal (5.314 registros, 30 columnas)
│   └── diccionario_variables.csv    # documentación de cada variable
├── analisis/
│   ├── index.qmd                    # resumen de la investigación
│   ├── articulo.qmd                 # panorama global y escala
│   ├── energia.qmd                  # consumo eléctrico y refrigeración
│   ├── agua.qmd                     # huella hídrica y riesgo de cuenca
│   ├── co2.qmd                      # emisiones e índice de impacto
│   ├── mapa.qmd                     # mapa multicapa
│   ├── denuncias.qmd                # conflictos socioambientales
│   ├── capital.qmd                  # inversión y concentración
│   ├── espacio_oceano.qmd           # alternativas de emplazamiento
│   ├── datos_formulas.qmd           # metodología y cascada de estimación
│   └── _quarto.yml                  # configuración del sitio
├── dc_estilos.py                    # paleta y configuración visual
└── README.md
```

Los análisis están en formato **Quarto** (`.qmd`): texto plano con celdas de Python, versionable y ejecutable. Se renderizan con `quarto render` o se pueden abrir como notebook en Jupyter.

---

## Reproducir el análisis

```bash
conda create -n datacenters python=3.11
conda activate datacenters
pip install pandas geopandas plotly matplotlib seaborn scikit-learn jupyterlab keplergl

cd analisis
quarto render
```

Requiere [Quarto](https://quarto.org/docs/get-started/) instalado. Los `.qmd` esperan `dc_trabajo.csv` en `../datos/` y `dc_estilos.py` en la raíz del proyecto.

---

## Algunos hallazgos

- El **27,5%** de los data centers operativos está sobre cuencas con estrés hídrico alto o extremadamente alto.
- Los **51 proyectos** en construcción y planificados documentados emitirían **198,7 millones de toneladas de CO₂/año**, contra 114,1 millones de los 5.263 operativos.
- El cruce espacial a nivel de subcuenca reclasificó el **72,8%** de los registros respecto del dato nacional, y elevó de 906 a 1.458 las instalaciones en estrés hídrico alto o extremo. El promedio país oculta la situación real de la cuenca.
- Para 2030 se proyecta un consumo de **9,3 billones de litros** de agua y más de **945 TWh** de electricidad anuales para el sector.

---

## Licencia y uso

El código y los datos derivados se publican bajo la licencia del repositorio. Los datos de origen mantienen las condiciones de sus fuentes: [PeeringDB](https://www.peeringdb.com/) y [WRI Aqueduct 4.0](https://www.wri.org/applications/aqueduct) tienen sus propios términos de uso.

Si usás este dataset, citá la investigación:

> Destéfanis, M. G. (2026). *Costo ambiental de la infraestructura de movimientos de datos*. D_Empathy Project. https://dempathyproject.com/investigaciones/datacenters/

---

## Contribuir

Es una investigación en curso. Correcciones al dataset, data centers faltantes, mejoras metodológicas y críticas al método son bienvenidas — abrí un issue o un pull request.

Si trabajás en un data center y tenés datos reales de consumo, ese aporte vale más que cualquier estimación.

---

**D_Empathy Project** — periodismo de datos independiente, abierto y colaborativo.
