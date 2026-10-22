"""Funciones de utilidad reutilizables."""

# pyrefly: ignore [missing-import]
import streamlit as st
from datetime import datetime


def format_number(value: float, decimals: int = 2) -> str:
    """Formatea un número con separadores de miles."""
    return f"{value:,.{decimals}f}"


def show_success(message: str) -> None:
    """Muestra un mensaje de éxito con estilo consistente."""
    st.success(f"✅ {message}")


def show_error(message: str) -> None:
    """Muestra un mensaje de error con estilo consistente."""
    st.error(f"❌ {message}")


def get_current_timestamp() -> str:
    """Devuelve la fecha y hora actual formateada."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
