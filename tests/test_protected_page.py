# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from streamlit.testing.v1 import AppTest

# Reemplaza esto con la ruta real de tu página protegida, por ejemplo: "pages/3_Perfil.py"
PROTECTED_PAGE_PATH = "pages/2_⚙️_Settings.py"

@pytest.mark.xfail(reason="Settings no implementa comprobación de autenticación")
def test_acceso_denegado_sin_login():
    """Prueba que un usuario sin sesión iniciada no pueda ver el contenido."""
    at = AppTest.from_file(PROTECTED_PAGE_PATH)
    
    # Nos aseguramos de que el session_state no tenga la clave 'usuario'
    if "usuario" in at.session_state:
        del at.session_state["usuario"]
        
    at.run()
    
    assert not at.exception
    # Comprobamos que muestre algún mensaje de error, advertencia o redirija
    # Por ejemplo, si usas st.error o st.warning para denegar el acceso:
    assert len(at.error) > 0 or len(at.warning) > 0
    # Alternativamente, comprobar un texto específico:
    # assert at.error[0].value == "Debes iniciar sesión para ver esta página."

def test_acceso_permitido_con_login():
    """Prueba que la página carga correctamente cuando el usuario está logueado."""
    at = AppTest.from_file(PROTECTED_PAGE_PATH)
    
    # Inicializamos el session_state simulando que el usuario ya ha iniciado sesión
    at.session_state["usuario"] = {
        "id": 1,
        "nombre": "Admin",
        "email": "admin@example.com"
    }
    
    at.run()
    
    assert not at.exception
    # Comprobamos que NO hay errores de acceso
    assert len(at.error) == 0
    assert len(at.warning) == 0
    
    # Comprobamos que carga el contenido protegido (por ejemplo, título o form)
    assert len(at.title) > 0
