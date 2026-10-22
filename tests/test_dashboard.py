# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from streamlit.testing.v1 import AppTest

DASHBOARD_PATH = "pages/1_📊_Dashboard.py"

def test_dashboard_carga_correctamente():
    """Prueba el happy path de carga del dashboard."""
    at = AppTest.from_file(DASHBOARD_PATH, default_timeout=10)
    at.run()
    assert not at.exception
    assert at.title[0].value == "📊 Dashboard Analítico"

def test_dashboard_filtro_texto():
    """Prueba el uso del filtro de texto para buscar en la tabla de datos."""
    at = AppTest.from_file(DASHBOARD_PATH)
    at.run()
    
    # Asume que el primer text_input es el filtro de la tabla
    at.text_input[0].set_value("búsqueda de prueba").run()
    assert not at.exception

def test_dashboard_filtro_vacio():
    """Prueba el edge case donde el filtro de texto está vacío."""
    at = AppTest.from_file(DASHBOARD_PATH)
    at.run()
    
    # Asume que el primer text_input es el filtro de la tabla
    at.text_input[0].set_value("").run()
    assert not at.exception

def test_dashboard_session_state():
    """Prueba de session_state para el dashboard."""
    at = AppTest.from_file(DASHBOARD_PATH)
    # Inicializamos el session_state como si el usuario ya hubiera interactuado
    at.session_state["filtro_texto"] = "búsqueda anterior"
    at.run()
    assert not at.exception
