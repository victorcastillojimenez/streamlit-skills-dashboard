import streamlit as st
from typing import Optional, Dict

def login_form(
    key_prefix: str = "login",
    title: str = "Iniciar Sesión",
    submit_button_text: str = "Entrar"
) -> Optional[Dict[str, str]]:
    """
    Renderiza un formulario de inicio de sesión con usuario y contraseña.

    Este componente muestra un formulario aislado utilizando `st.form`. 
    Captura el nombre de usuario y la contraseña y los devuelve al ser enviado.

    Args:
        key_prefix: Prefijo único para evitar colisiones de estado si se usa múltiples veces.
        title: Título que se mostrará encima del formulario.
        submit_button_text: Texto para el botón de envío del formulario.

    Returns:
        Un diccionario con las claves 'username' y 'password' si el formulario 
        fue enviado, o None si aún no se ha enviado.

    Session State:
        Reads: st.session_state["{key_prefix}_username"] — para leer el usuario en el formulario.
        Reads: st.session_state["{key_prefix}_password"] — para leer la contraseña en el formulario.
        Writes: st.session_state["{key_prefix}_username"] — al escribir en el campo de usuario.
        Writes: st.session_state["{key_prefix}_password"] — al escribir en el campo de contraseña.
    """
    st.subheader(title)
    
    # Usar st.form asegura que los inputs se agrupen y no recarguen la app al escribir
    with st.form(key=f"{key_prefix}_form"):
        username = st.text_input(
            "Usuario",
            placeholder="Introduce tu usuario",
            key=f"{key_prefix}_username"
        )
        
        password = st.text_input(
            "Contraseña",
            type="password",
            placeholder="Introduce tu contraseña",
            key=f"{key_prefix}_password"
        )
        
        submitted = st.form_submit_button(submit_button_text)
        
        if submitted:
            return {"username": username, "password": password}
            
    return None
