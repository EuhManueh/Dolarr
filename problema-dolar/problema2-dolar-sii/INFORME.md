# INFORME – Laboratorio de Computación Numérica 1

## 1. Objetivo
Se estudia el dólar observado promedio mensual del SII entre enero de 2022 y diciembre de 2025. El enunciado exige analizar representación con pocas cifras significativas, error absoluto y relativo, propagación, cancelación y punto flotante. 

## 2. A1 – Error de representación
Para cada dato se calculó Ea=|P-Paprox| y Er=Ea/|P|×100. Al usar 2 cifras significativas, el mayor error relativo corresponde a **Abril 2022**, con **0.5987%**.

## 3. A2 – Compra y venta
Para la mejor operación retrospectiva se compra en **Febrero 2023 798.26 CLP/USD** y se vende en **Enero 2025 1000.76 CLP/USD**.

Con los valores aproximados de 2 cifras:
- USD = M/Pcompra ≈ **1,250.00 USD**
- Pesos finales ≈ **$1,250,000.00**
- Ganancia ≈ **$250,000.00**
- Ganancia con error ≈ **$250,000.00 ± $3,673.95**
- Rentabilidad ≈ **25.00% ± 0.37%**

El enunciado establece división para comprar, multiplicación para vender y resta para la ganancia.

## 4. A3 – Cancelación
Para diciembre 2022 y diciembre 2023:
ΔP = 874.67 − 875.66.

Con 3 cifras significativas:
**ΔP = -1.00 CLP ± 0.67 CLP**, con error porcentual **67.00%**.

Como la incertidumbre es comparable/mayor que la magnitud de la diferencia, **no se puede afirmar con seguridad que el dólar subió o bajó**. 

## 5. A4 – Anualidad
Orden de confiabilidad, de menor a mayor error porcentual: **2025, 2024, 2022, 2023**.

| Año | Variación | Error | Error % |
|---|---:|---:|---:|
| 2025 | -80.00 | ±4.60 | 5.75% |\n| 2024 | 70.00 | ±4.31 | 6.16% |\n| 2022 | 60.00 | ±6.39 | 10.65% |\n| 2023 | 40.00 | ±8.33 | 20.82% |\n
Los años menos confiables tienen variaciones enero→diciembre pequeñas frente al error de representación; la resta de valores grandes y parecidos amplifica la incertidumbre relativa.

## 6. A5 – Mejor compra y mejor venta
El mínimo fue **Febrero 2023 ($798.26)** y el máximo fue **Enero 2025 ($1000.76)**.

La estrategia mínimo→máximo produce **25.00% ± 0.37%**. La diferencia es mucho mayor que la incertidumbre, por lo que esta conclusión retrospectiva **sí sobrevive al error**. El enunciado solicita precisamente comprobar si la conclusión sobrevive a la incertidumbre.

## 7. B1 – Mantisa corta
Según la convención del laboratorio, usar pocas cifras significativas representa una mantisa corta. Para 1000.76, con 3 cifras significativas: **1.00×10³ = 1000**, con error absoluto **0.76**. 

## 8. B2 – Ida y vuelta
Se calculó pesos→dólares→pesos con float32 y float64 para los 48 precios. En aritmética exacta debería recuperarse exactamente el monto inicial; en punto flotante aparecen pequeñas derivas por redondeo. La gráfica correspondiente es `05_ida_vuelta_float.png`. El ejercicio pide repetir el ciclo para los distintos precios y comparar su comportamiento con la curva temporal. 

## 9. B4 – Cancelación en máquina
- float32: **-0.9899902344**
- float64: **-0.990000000000009**

La resta conserva más cifras en float64. El resultado conecta con A3: una diferencia pequeña entre números relativamente grandes puede tener baja confiabilidad relativa. 

## 10. Conclusión
El período analizado muestra que el dólar fue más barato en **Febrero 2023** y más caro en **Enero 2025**. La operación retrospectiva de comprar en el mínimo y vender en el máximo entrega una rentabilidad de **25.00% ± 0.37%**, suficientemente grande para superar la incertidumbre calculada.

En contraste, diciembre de 2022 frente a diciembre de 2023 constituye un caso de cancelación: la diferencia es pequeña frente al error, por lo que no corresponde afirmar con seguridad una subida o bajada. La lección central es que **una diferencia entre dos números grandes y parecidos puede perder cifras significativas y volverse poco confiable si no se compara con su incertidumbre**.

## 11. Gráficas obligatorias
Se incluyen las cinco gráficas solicitadas por el enunciado: serie mensual, variación mensual, error de representación, rentabilidad desde el mínimo e ida/vuelta en punto flotante. 
