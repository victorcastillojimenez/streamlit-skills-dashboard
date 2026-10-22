"""Punto de entrada principal de la aplicación Streamlit."""

# pyrefly: ignore [missing-import]
import streamlit as st

st.set_page_config(
    page_title="Mi App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://docs.streamlit.io",
        "Report a bug": None,
        "About": "# Mi App\nGenerado con streamlit-bootstrap.",
    },
)

# Inicializar estado de sesión global
if "user" not in st.session_state:
    st.session_state.user = "Invitado"

# Página de bienvenida (Home)
st.title("🚀 Mi App")
st.markdown(
    """
    Bienvenido a tu nueva aplicación Streamlit multipágina.
    Usa el menú de la **izquierda** para navegar entre secciones.

    ### Cómo empezar
    1. Edita `app.py` para personalizar esta página de inicio.
    2. Añade nuevas páginas en la carpeta `pages/`.
    3. Crea componentes reutilizables en `components/`.
    4. Coloca tu lógica de negocio en `utils/`.
    5. Configura tu tema en `.streamlit/config.toml`.
    """
)

st.info(
    "📝 Copia `.streamlit/secrets.toml.example` a `.streamlit/secrets.toml` "
    "y añade tus credenciales reales antes de continuar.",
    icon="🔐",
)
