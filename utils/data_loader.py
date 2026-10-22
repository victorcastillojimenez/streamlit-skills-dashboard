import pandas as pd
import numpy as np
from datetime import date, timedelta

def generate_mock_data() -> pd.DataFrame:
    """Genera datos simulados para el dashboard y los reportes."""
    np.random.seed(42)
    dates = [date.today() - timedelta(days=i) for i in range(30)]
    categories = ["Electrónica", "Ropa", "Hogar", "Juguetes"]
    
    data = []
    for d in dates:
        for c in categories:
            data.append({
                "Fecha": d,
                "Categoría": c,
                "Ventas": int(np.random.randint(100, 5000)),
                "Visitas": int(np.random.randint(500, 10000))
            })
    return pd.DataFrame(data)
