from pathlib import Path
import numpy as np

# Definición de rutas utilizando pathlib
BASE_DIR = Path(__file__).resolve().parent
PATH_CSV = BASE_DIR.parent / 'data' / 'dolar_observado_sii_2022_2025.csv'

# Carga de datos de precios
precios = np.loadtxt(PATH_CSV, delimiter=',', skiprows=1, usecols=3)

def aplicar_redondeo_sig(val, n_sig=2):
    """Redondea un número a n cifras significativas."""
    if np.isnan(val) or val == 0:
        return val
    exponente = np.floor(np.log10(np.abs(val)))
    precision = int(n_sig - 1 - exponente)
    return np.round(val, precision)

# Vectorización de la función de redondeo
redondear_vec = np.vectorize(aplicar_redondeo_sig)
# Alias para mantener compatibilidad si es llamado externamente
redondear_simple = aplicar_redondeo_sig
carpeta_src = str(BASE_DIR)