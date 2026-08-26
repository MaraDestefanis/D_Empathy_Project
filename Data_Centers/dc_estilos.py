"""
dc_estilos.py — Paleta y configuración visual centralizada
Investigación D_Empathy Project · Data Centers & Impacto Ambiental
Importar al inicio de cada notebook: from dc_estilos import *
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

# ── Paleta D_Empathy ──────────────────────────────────────────────────────────
PALETA = {
    "hueso":   "#F2EFE4",   # fondo suave
    "oliva":   "#7C8C5E",   # color principal
    "tierra":  "#A0785A",   # acento cálido
    "musgo":   "#4F6347",   # oscuro natural
    "pizarra": "#5A6472",   # neutro azulado
    "crema":   "#D9D2C0",   # secundario claro
    "ink":     "#2C2C2C",   # texto
    "azul_grisaceo": "#6B8C9E", #  marcar en energia 
}

# ── Colores por tamaño de DC (coherentes con paleta D_Empathy) ────────────────
COLOR_TAMAÑO = {
    "small":      "#A8C5A0",   # verde claro / oliva suave
    "medium":     "#7C8C5E",   # oliva
    "large":      "#A0785A",   # tierra
    "hyperscale": "#4F6347",   # musgo oscuro
}
ORDEN_TAMAÑO = ["small", "medium", "large", "hyperscale"]


# ── Colores por tamaño_categoria (megaproyectos) ──────────────────────────────
COLOR_TAMAÑO = {
    "hyperscale":  "#ff4800",   # naranja-rojo destacado
    "large":       "#f4a261",   # naranja suave
    "medium":      "#e9c46a",   # amarillo
    "sin_dato":    "#adb5bd",   # gris claro
}
ORDEN_TAMAÑO_CAT = ["hyperscale", "large", "medium", "sin_dato"]


# ── Colores por estado ────────────────────────────────────────────────────────
COLOR_ESTADO = {
    "operativo":    "#6B8C9E",   # azul grisáceo
    "construccion": "#E63946",   # rojo fuerte
    "planificado":  "#F4A261",   # naranja
}
ORDEN_ESTADO = ["operativo", "construccion", "planificado"]

# ── Colores por continente ────────────────────────────────────────────────────
COLOR_CONTINENTE = {
    "América del Norte": "#7C8C5E",
    "Europa":            "#A0785A",
    "Asia-Pacífico":     "#5A6472",
    "América del Sur":   "#A8C5A0",
    "Australia":         "#D9D2C0",
    "África":            "#4F6347",
    "Oriente Medio":     "#C4A882",
}


# ── Colores por refrigerio
#────────────────────────────────────────────────────
COLOR_REFRIG = {
    "aire":                     "#E63946",
    "evaporativa (agua)":       "#1D7484",
    "mixto":                    "#9D9D9D",
    "aire/hibrido (post-2024)": "#FF8C42",
}
ORDEN_REFRIG = ["aire", "evaporativa (agua)", "mixto", "aire/hibrido (post-2024)"]

# ── Paleta secuencial (para facetados multi-serie) ────────────────────────────
COLORES_SEQ = [
    PALETA["oliva"],
    PALETA["tierra"],
    PALETA["pizarra"],
    PALETA["musgo"],
    PALETA["crema"],
]

# ── Template Plotly coherente con D_Empathy ───────────────────────────────────
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
from plotly.subplots import make_subplots
from IPython.display import display, HTML


pio.templates["dempathy"] = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor="#F2EFE4",
        plot_bgcolor="#F2EFE4",
        font=dict(family="Georgia, serif", color="#2C2C2C", size=11),
        title=dict(font=dict(size=14, color="#2C2C2C")),
        colorway=[
            "#7C8C5E","#A0785A","#5A6472",
            "#4F6347","#D9D2C0","#A8C5A0","#C4A882"
        ],
        xaxis=dict(
            gridcolor="#D9D2C0", gridwidth=0.5,
            linecolor="#2C2C2C", linewidth=0.7,
            showgrid=True,
        ),
        yaxis=dict(
            gridcolor="#D9D2C0", gridwidth=0.5,
            linecolor="#2C2C2C", linewidth=0.7,
            showgrid=True,
        ),
        legend=dict(bgcolor="rgba(242,239,228,0.8)", bordercolor="#D9D2C0"),
    )
)
TEMPLATE_PLOTLY = "dempathy"

COLOR_TAMAÑO_R = {
    "local":          "#6c757d",   # gris
    "regional":       "#4895ef",   # azul
    "nacional":       "#4cc9f0",   # celeste
    "internacional":  "#f77f00",   # naranja fuerte
}

ORDEN_TAMAÑO_R = ['local', 'regional', 'nacional', 'internacional']


# ── rcParams matplotlib ───────────────────────────────────────────────────────
sns.set_theme(style="ticks")
plt.rcParams.update({
    "figure.dpi":        130,
    "figure.facecolor":  "white",
    "axes.facecolor":    "white",
    "axes.edgecolor":    PALETA["ink"],
    "axes.linewidth":    0.7,
    "axes.spines.top":   False,
    "axes.spines.right": False,
    "axes.titlesize":    11,
    "axes.titleweight":  "regular",
    "axes.labelsize":    9,
    "axes.labelcolor":   PALETA["ink"],
    "xtick.labelsize":   8,
    "ytick.labelsize":   8,
    "xtick.color":       PALETA["ink"],
    "ytick.color":       PALETA["ink"],
    "grid.color":        PALETA["crema"],
    "grid.linewidth":    0.5,
    "grid.linestyle":    "--",
    "legend.fontsize":   8,
    "legend.frameon":    False,
    "font.family":       "serif",
})

print("Estilo D_Empathy cargado.")
