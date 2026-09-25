import numpy as np
from cargar_datos import precios, redondear_vec

print("=== B4: EVALUACIÓN DE PRECISIÓN DE FLOTANTES ===")
val_a, val_b = 874.67, 875.66

# Comparativo float32 vs float64
dif_f32 = np.float32(val_a) - np.float32(val_b)
dif_f64 = np.float64(val_a) - np.float64(val_b)

print("Resultado teórico esperado: -0.99")
print(f"Resultado en Precisión Simple (float32): {dif_f32}")
print(f"Resultado en Doble Precisión (float64):  {dif_f64}")

print("\n=== B2: IMPACTO DE PÉRDIDA POR TRUNCAMIENTO ===")
MONTO = 1000000
precios_aprox = redondear_vec(precios)

# Simulación de ida y vuelta inmediata
usd = redondear_vec(MONTO / precios_aprox)
retorno_clp = redondear_vec(usd * precios_aprox)
perdida = MONTO - retorno_clp

print(f"Capital base: ${MONTO:,} CLP")
print(f"Pérdida por redondeo (Enero 2022): ${perdida[0]:.2f}")
print(f"Pérdida máxima observada: ${np.max(perdida):.2f}")