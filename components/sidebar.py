"""Sidebar compartido entre páginas."""

# pyrefly: ignore [missing-import]
import streamlit as st


def render_sidebar() -> None:
    """Renderiza la barra lateral con navegación y opciones globales."""
    with st.sidebar:
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50)
        st.title("Mi App")
        st.markdown("---")

        st.markdown("### ⚙️ Opciones globales")
        theme = st.selectbox("Tema", ["Oscuro", "Claro"], key="global_theme")
        st.markdown("---")

        st.caption(f"v1.0.0 · {st.session_state.get('user', 'Invitado')}")
