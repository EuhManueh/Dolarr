from cargar_datos import precios, aplicar_redondeo_sig

print("=== [A4] ANÁLISIS DE CONFIAZA DE VARIACIONES ANUALES ===")

anios = [2022, 2023, 2024, 2025]
m_ene = [0, 12, 24, 36]
m_dic = [11, 23, 35, 47]

métricas_anuales = []

for yr, idx_e, idx_d in zip(anios, m_ene, m_dic):
    p_e, p_d = precios[idx_e], precios[idx_d]
    
    # Redondeo a 2 cifras significativas
    p_e_aprox = aplicar_redondeo_sig(p_e, n_sig=2)
    p_d_aprox = aplicar_redondeo_sig(p_d, n_sig=2)
    
    # Errores individuales
    err_abs_e = abs(p_e - p_e_aprox)
    err_abs_d = abs(p_d - p_d_aprox)
    
    # Variación y propagación del error absoluto
    variacion = p_d_aprox - p_e_aprox
    err_abs_var = err_abs_e + err_abs_d
    
    # Error relativo
    err_rel_var = (err_abs_var / abs(variacion)) * 100.0 if variacion != 0 else float('inf')
    
    métricas_anuales.append({
        'anio': yr,
        'delta': variacion,
        'err_abs': err_abs_var,
        'err_rel': err_rel_var
    })

# Ordenar por precisión/confiabilidad (menor error relativo)
métricas_ordenadas = sorted(métricas_anuales, key=lambda x: x['err_rel'])

print("Jerarquía de años (Menor a Mayor error relativo):")
for item in métricas_ordenadas:
    print(f"• Año {item['anio']}: Variación = {item['delta']:.2f} ± {item['err_abs']:.2f} CLP | Error Relativo = {item['err_rel']:.2f}%")