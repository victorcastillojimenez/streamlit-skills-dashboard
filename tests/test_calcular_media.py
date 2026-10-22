import pytest

def calcular_media(valores: list[float]) -> float:
    return sum(valores) / len(valores)

def test_calcular_media_valores_normales():
    """Prueba el cálculo de la media con una lista de valores positivos."""
    assert calcular_media([10.0, 20.0, 30.0]) == 20.0

def test_calcular_media_valores_negativos():
    """Prueba el cálculo con valores negativos y mixtos."""
    assert calcular_media([-10.0, 10.0, 0.0]) == 0.0

def test_calcular_media_un_solo_valor():
    """Prueba que si hay un solo valor, la media es ese mismo valor."""
    assert calcular_media([42.5]) == 42.5

def test_calcular_media_lista_vacia():
    """Prueba que lance ZeroDivisionError si la lista está vacía."""
    with pytest.raises(ZeroDivisionError):
        calcular_media([])
