import streamlit as st
import pandas as pd

def filtered_table(
    df: pd.DataFrame,
    key_prefix: str = "filtered_table",
    filter_placeholder: str = "Buscar...",
    columns_to_filter: list[str] | None = None
) -> pd.DataFrame:
    """
    Renderiza una tabla con un campo de texto para filtrar los resultados.

    Permite al usuario filtrar un DataFrame buscando un texto en todas sus columnas 
    de tipo texto, o en un subconjunto específico de columnas.

    Args:
        df: El DataFrame de pandas a mostrar y filtrar.
        key_prefix: Prefijo único para evitar colisiones de estado si se usa múltiples veces.
        filter_placeholder: Texto de ayuda (placeholder) para el campo de búsqueda.
        columns_to_filter: Lista opcional de nombres de columnas donde buscar. Si es None, busca en todas las columnas string.

    Returns:
        El DataFrame filtrado que se está mostrando actualmente en la tabla.

    Session State:
        Reads: st.session_state["{key_prefix}_search"] — para obtener el texto de búsqueda actual.
        Writes: st.session_state["{key_prefix}_search"] — al actualizar el campo de texto.
    """
    search_key = f"{key_prefix}_search"
    
    # Campo de texto para la búsqueda
    search_term = st.text_input(
        "🔎 Filtrar datos:",
        placeholder=filter_placeholder,
        key=search_key
    )
    
    # Filtrar el dataframe
    filtered_df = df.copy()
    if search_term:
        # Convertir el texto de búsqueda a minúsculas
        search_term_lower = search_term.lower()
        
        # Determinar en qué columnas buscar
        if columns_to_filter is None:
            # Seleccionar solo las columnas que son de tipo object/string por defecto
            cols = filtered_df.select_dtypes(include=['object', 'string']).columns
        else:
            cols = columns_to_filter
            
        # Crear una máscara booleana, iniciada en False
        mask = pd.Series(False, index=filtered_df.index)
        
        for col in cols:
            if col in filtered_df.columns:
                # Actualizar la máscara usando OR lógico
                # Convertimos la columna a string para buscar texto de manera segura
                mask |= filtered_df[col].astype(str).str.lower().str.contains(search_term_lower, na=False)
                
        filtered_df = filtered_df[mask]
        
    # Mostrar el dataframe filtrado
    st.dataframe(filtered_df, use_container_width=True)
    
    return filtered_df
