import csv
from pathlib import Path
import numpy as np

from cargar_datos import precios, redondear_vec, aplicar_redondeo_sig, BASE_DIR

print("=== REPORTE DE ANÁLISIS DE ERRORES ===")

# --- A1: EVALUACIÓN DE REPRESENTACIÓN ---
precios_est = redondear_vec(precios)
err_abs = np.abs(precios - precios_est)
err_rel_pct = (err_abs / precios) * 100.0

idx_max_err = np.nanargmax(err_rel_pct)

print("\n--- [A1] Error de Representación Máximo ---")
print(f"Índice de mes crítico: {idx_max_err}")
print(f"Valor real vs Aproximado: {precios[idx_max_err]} -> {precios_est[idx_max_err]}")
print(f"Error relativo máximo: {err_rel_pct[idx_max_err]:.4f}%")

# --- A2: OPERACIÓN ENE 2022 A JUL 2022 ---
print("\n--- [A2] Simulación Compra/Venta (Ene 2022 - Jul 2022) ---")
MONTO_INICIAL = 1000000
idx_in, idx_out = 0, 6

p_in_est = precios_est[idx_in]
p_out_est = precios_est[idx_out]

e_rel_in = err_rel_pct[idx_in] / 100.0
e_rel_out = err_rel_pct[idx_out] / 100.0

divisas_obtenidas = MONTO_INICIAL / p_in_est
monto_final_est = divisas_obtenidas * p_out_est

e_rel_final = e_rel_in + e_rel_out
e_abs_final = e_rel_final * monto_final_est

utilidad_est = monto_final_est - MONTO_INICIAL
e_abs_utilidad = e_abs_final
e_rel_utilidad_pct = (e_abs_utilidad / abs(utilidad_est)) * 100.0

print(f"Ganancia estimada: ${utilidad_est:.2f}")
print(f"Error absoluto ganancia: ± ${e_abs_utilidad:.2f}")
print(f"Margen de error: {e_rel_utilidad_pct:.2f}%")

# --- A3: ANÁLISIS DE CANCELACIÓN CATASTRÓFICA ---
print("\n--- [A3] Variación Interanual (Dic 2022 - Dic 2023) ---")
val_dic22, val_dic23 = 875.66, 874.67

dic22_est = aplicar_redondeo_sig(val_dic22, n_sig=3)
dic23_est = aplicar_redondeo_sig(val_dic23, n_sig=3)

e_abs_dic22 = abs(val_dic22 - dic22_est)
e_abs_dic23 = abs(val_dic23 - dic23_est)

delta_precio = dic23_est - dic22_est
e_abs_delta = e_abs_dic22 + e_abs_dic23
e_rel_delta_pct = (e_abs_delta / abs(delta_precio)) * 100.0

print(f"ΔP Calculado: {delta_precio:.2f} ± {e_abs_delta:.2f} CLP")
print(f"Error relativo de la variación: {e_rel_delta_pct:.2f}%")

# --- A5: OPTIMIZACIÓN DE OPERACIONES (MEJOR COMPRA/VENTA) ---
print("\n--- [A5] Mejor Escenario Histórico ---")
idx_min_p, idx_max_p = np.nanargmin(precios), np.nanargmax(precios)

p_min_est, p_max_est = precios_est[idx_min_p], precios_est[idx_max_p]
e_rel_min, e_rel_max = err_rel_pct[idx_min_p] / 100.0, err_rel_pct[idx_max_p] / 100.0

divisas_opt = MONTO_INICIAL / p_min_est
monto_opt_final = divisas_opt * p_max_est

e_rel_opt = e_rel_min + e_rel_max
e_abs_opt = e_rel_opt * monto_opt_final

utilidad_opt = monto_opt_final - MONTO_INICIAL
e_abs_utilidad_opt = e_abs_opt
rentabilidad_pct = (utilidad_opt / MONTO_INICIAL) * 100.0
e_abs_rentabilidad_pct = (e_abs_utilidad_opt / MONTO_INICIAL) * 100.0

print(f"Ganancia óptima: ${utilidad_opt:.2f} ± ${e_abs_utilidad_opt:.2f}")
print(f"Rentabilidad: {rentabilidad_pct:.2f}% ± {e_abs_rentabilidad_pct:.2f}%")

# --- GUARDAR DATOS EN ARCHIVO ---
path_salida = BASE_DIR.parent / 'data' / 'tabla_errores.csv'
filas = [
    ['Evaluacion', 'Error Absoluto (CLP)', 'Error Relativo (%)', 'Error Propagado (CLP)'],
    ['A2: Compra Ene 22 - Venta Jul 22', f"{e_abs_utilidad:.2f}", f"{e_rel_utilidad_pct:.2f}", f"{e_abs_utilidad:.2f}"],
    ['A3: Variacion Dic 22 - Dic 23', f"{e_abs_delta:.2f}", f"{e_rel_delta_pct:.2f}", f"{e_abs_delta:.2f}"],
    ['A5: Mejor Compra - Mejor Venta', f"{e_abs_utilidad_opt:.2f}", f"{e_abs_rentabilidad_pct:.2f}", f"{e_abs_utilidad_opt:.2f}"]
]

with open(path_salida, mode='w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerows(filas)

print(f"\n[OK] Archivo exportado exitosamente en: {path_salida}")
