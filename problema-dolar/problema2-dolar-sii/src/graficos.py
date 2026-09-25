import numpy as np
import matplotlib.pyplot as plt
import os
from cargar_datos import precios, redondear_vec

print("--- GENERANDO LOS 5 GRÁFICOS OBLIGATORIOS ---")

carpeta_src = os.path.dirname(os.path.abspath(__file__))
carpeta_graficos = os.path.join(carpeta_src, '..', 'graficos')

precios_aprox = redondear_vec(precios)
ea = np.abs(precios - precios_aprox)
er = (ea / precios) * 100
meses_total = np.arange(1, 49)
M = 1000000


# --- GRÁFICO 1: SERIE MENSUAL DEL DÓLAR OBSERVADO 2022-2025 ---

plt.figure(figsize=(10, 5))

plt.plot(
    meses_total,
    precios,
    marker='o',
    linestyle='-',
    color='b',
    label='Dólar Observado (Real)'
)

plt.title('Serie mensual del dólar observado 2022-2025')
plt.xlabel('Meses (Enero 2022 - Diciembre 2025)')
plt.ylabel('Precio (CLP)')

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.savefig(
    os.path.join(
        carpeta_graficos,
        'grafico1_serie_mensual.png'
    )
)

plt.close()


# --- GRÁFICO 2: VARIACIÓN MES A MES (CANCELACIÓN) ---

delta_p = np.diff(precios_aprox)

ea_delta = ea[1:] + ea[:-1]

meses_diff = np.arange(2, 49)


plt.figure(figsize=(10, 5))

plt.bar(
    meses_diff,
    delta_p,
    yerr=ea_delta,
    capsize=3,
    color='coral',
    edgecolor='black',
    alpha=0.8
)

plt.axhline(
    0,
    color='black',
    linewidth=1
)

plt.title(
    r'Variación mes a mes con Error Propagado (Cancelación)'
)

plt.xlabel(
    'Meses (Febrero 2022 - Diciembre 2025)'
)

plt.ylabel(
    'Variación en pesos (CLP)'
)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.6
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        carpeta_graficos,
        'grafico2_variacion.png'
    )
)

plt.close()


# --- GRÁFICO 3: ERROR DE REPRESENTACIÓN POR MES ---

plt.figure(figsize=(10, 5))

plt.bar(
    meses_total,
    ea,
    color='purple',
    edgecolor='black',
    alpha=0.7
)

plt.title(
    'Error Absoluto de Representación por Mes (2 cifras significativas)'
)

plt.xlabel(
    'Meses (Enero 2022 - Diciembre 2025)'
)

plt.ylabel(
    'Error Absoluto (CLP perdidos por redondeo)'
)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.6
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        carpeta_graficos,
        'grafico3_error_rep.png'
    )
)

plt.close()


# --- GRÁFICO 4: RENTABILIDAD DESDE EL MÍNIMO ---

idx_min = np.nanargmin(precios)

p_min_aprox = precios_aprox[idx_min]

er_min = er[idx_min] / 100


meses_post = np.arange(
    idx_min + 2,
    49
)

p_ventas_aprox = precios_aprox[idx_min + 1:]

er_ventas = er[idx_min + 1:] / 100


usd = M / p_min_aprox

er_usd = er_min

pesos_final = usd * p_ventas_aprox

er_pesos = er_usd + er_ventas

ea_pesos = er_pesos * pesos_final


ganancia = pesos_final - M

ea_ganancia = ea_pesos

rentabilidad = (ganancia / M) * 100

ea_rent = (ea_ganancia / M) * 100


plt.figure(figsize=(10, 5))

plt.errorbar(
    meses_post,
    rentabilidad,
    yerr=ea_rent,
    fmt='o-',
    color='green',
    ecolor='red',
    capsize=4,
    label='Rentabilidad (%)'
)

plt.axhline(
    0,
    color='black',
    linewidth=1
)

plt.title(
    'Rentabilidad invirtiendo $1.000.000 en el mínimo histórico'
)

plt.xlabel(
    'Meses posteriores a la compra'
)

plt.ylabel(
    'Rentabilidad (%)'
)

plt.legend()

plt.grid(
    True,
    linestyle='--',
    alpha=0.6
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        carpeta_graficos,
        'grafico4_rentabilidad.png'
    )
)

plt.close()


# --- GRÁFICO 5: DERIVA DE LA IDA Y VUELTA (B2) ---

usd_comprados = redondear_vec(
    M / precios_aprox
)

pesos_recuperados = redondear_vec(
    usd_comprados * precios_aprox
)


fig, ax1 = plt.subplots(
    figsize=(10, 6)
)

color1 = 'tab:blue'

ax1.set_xlabel(
    'Meses (Enero 2022 - Diciembre 2025)'
)

ax1.set_ylabel(
    'Precio Dólar (CLP)',
    color=color1
)

ax1.plot(
    meses_total,
    precios_aprox,
    color=color1,
    marker='o',
    label='Precio Dólar (2 cifras)'
)

ax1.tick_params(
    axis='y',
    labelcolor=color1
)


ax2 = ax1.twinx()

color2 = 'tab:red'

ax2.set_ylabel(
    'Pesos Recuperados tras Ida y Vuelta',
    color=color2
)

ax2.plot(
    meses_total,
    pesos_recuperados,
    color=color2,
    marker='x',
    linestyle='dashed',
    label='Pesos Recuperados'
)

ax2.tick_params(
    axis='y',
    labelcolor=color2
)

ax2.axhline(
    y=1000000,
    color='green',
    linestyle=':',
    label='Monto Original ($1.000.000)'
)


plt.title(
    'Deriva de la ida y vuelta en Punto Flotante vs Precio del Dólar'
)

fig.tight_layout()

plt.grid(
    True,
    linestyle='--',
    alpha=0.6
)

plt.savefig(
    os.path.join(
        carpeta_graficos,
        'grafico5_ida_y_vuelta.png'
    )
)

plt.close()


print(
    "Las 5 imagenes se guardaron correctamente en: ",
    carpeta_graficos
)