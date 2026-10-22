"""Página de configuración de la aplicación."""

# pyrefly: ignore [missing-import]
import streamlit as st
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Configuración",
    page_icon="⚙️",
    layout="wide",
)

render_sidebar()

st.title("⚙️ Configuración")

with st.form("settings_form"):
    st.subheader("Perfil de usuario")
    nombre = st.text_input("Nombre", placeholder="Tu nombre")
    email = st.text_input("Email", placeholder="tu@email.com")

    st.subheader("Preferencias")
    notificaciones = st.toggle("Activar notificaciones", value=True)
    idioma = st.selectbox("Idioma", ["Español", "English", "Français"])

    submitted = st.form_submit_button("💾 Guardar cambios", type="primary")
    if submitted:
        st.success("✅ Configuración guardada correctamente.")
