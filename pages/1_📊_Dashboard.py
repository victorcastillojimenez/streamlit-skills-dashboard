"""Página principal del dashboard."""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta

# Importamos los componentes y utilidades locales
from components.sidebar import render_sidebar
from components.filtered_table import filtered_table
from utils.helpers import format_number
from utils.data_loader import generate_mock_data

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
)

# 1. Renderizamos la opciones globales del sidebar
render_sidebar()

st.title("📊 Dashboard Analítico")
st.markdown("Bienvenido a tu dashboard. Analiza los datos usando los filtros interactivos disponibles en la barra lateral.")

# --- DATOS DE EJEMPLO ---
@st.cache_data
def load_data() -> pd.DataFrame:
    """Carga los datos simulados para el dashboard y los cachea."""
    return generate_mock_data()

df = load_data()

# --- SIDEBAR CON FILTROS ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Filtros del Dashboard")

# Filtro por categoría
categorias_disponibles = df["Categoría"].unique().tolist()
categorias_seleccionadas = st.sidebar.multiselect(
    "Selecciona Categorías",
    options=categorias_disponibles,
    default=categorias_disponibles
)

# Filtro por rango de ventas
ventas_min, ventas_max = st.sidebar.slider(
    "Rango de Ventas",
    min_value=int(df["Ventas"].min()),
    max_value=int(df["Ventas"].max()),
    value=(int(df["Ventas"].min()), int(df["Ventas"].max()))
)

# --- APLICAR FILTROS ---
df_filtrado = df[
    (df["Categoría"].isin(categorias_seleccionadas)) &
    (df["Ventas"] >= ventas_min) &
    (df["Ventas"] <= ventas_max)
]

# --- MÉTRICAS ---
st.subheader("Resumen General")
col1, col2, col3, col4 = st.columns(4)

ventas_totales = df_filtrado["Ventas"].sum()
visitas_totales = df_filtrado["Visitas"].sum()
ticket_promedio = ventas_totales / visitas_totales if visitas_totales > 0 else 0

with col1:
    st.metric("Ventas Totales", f"${format_number(ventas_totales, decimals=0)}")
with col2:
    st.metric("Visitas Totales", format_number(visitas_totales, decimals=0))
with col3:
    st.metric("Ticket Promedio", f"${ticket_promedio:.2f}")
with col4:
    st.metric("Registros", len(df_filtrado))

st.markdown("---")

# --- GRÁFICOS ---
st.subheader("Tendencia de Ventas y Visitas")
tab1, tab2 = st.tabs(["📈 Evolución Temporal", "📊 Por Categoría"])

with tab1:
    # Agrupar por fecha
    df_tendencia = df_filtrado.groupby("Fecha")[["Ventas", "Visitas"]].sum().reset_index()
    if not df_tendencia.empty:
        st.line_chart(data=df_tendencia.set_index("Fecha"), use_container_width=True)
    else:
        st.warning("No hay datos para mostrar con los filtros actuales.")

with tab2:
    # Agrupar por categoría
    df_cat = df_filtrado.groupby("Categoría")[["Ventas"]].sum().reset_index()
    if not df_cat.empty:
        st.bar_chart(data=df_cat.set_index("Categoría"), use_container_width=True)
    else:
        st.warning("No hay datos para mostrar con los filtros actuales.")

st.markdown("---")

# --- TABLA DE DATOS ---
st.subheader("Detalle de Datos")
st.markdown("Explora los registros individuales usando la búsqueda rápida de la tabla:")

# Utilizamos el componente reutilizable `filtered_table`
df_final = filtered_table(
    df=df_filtrado,
    key_prefix="dashboard_table",
    filter_placeholder="Buscar por categoría...",
    columns_to_filter=["Categoría"]
)
