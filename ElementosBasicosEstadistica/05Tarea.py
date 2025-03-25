import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('ElementosBasicosEstadistica/Datos_Con_Sucursal.csv')

# 1. Conocer las ventas totales del comercio
ventas_tot = df["ventas_tot"].sum()
print('La suma de las ventas totales es:', ventas_tot)

# 2. Conocer cuantos socios tienen adeudo y cuantos no tienen adeudo con su porcentaje correspondiente
tot_adeudo = df[df["adeudo_actual"] > 0].shape[0]
tot_no_adeudo = df[df["adeudo_actual"] == 0].shape[0]

porcen_adeudo = (tot_adeudo / len(df)) * 100
porcen_no_adeudo = (tot_no_adeudo / len(df)) * 100

print('La cantidad de socios con adeudos:', tot_adeudo, '(', round(porcen_adeudo, 2), '%)')
print('La cantidad de socios sin adeudos:', tot_no_adeudo, '(', round(porcen_no_adeudo, 2), '%)')

# 3. Grafica donde se pueda observar las ventas totales respecto del tiempo, en una grafica de barras 
plt.figure(figsize=(10, 5))
plt.bar(df["B_mes"], df["ventas_tot"], color='blue')
plt.xlabel("Fecha")
plt.ylabel("Ventas Totales")
plt.title("Ventas Totales respecto al Tiempo")
plt.xticks(rotation=45)
plt.show()

# 4. Grafica donde se pueda visualizar la desviación estándar de los pagos realizados del comercio respecto del tiempo
std_pagos = df.groupby("B_mes")["pagos_tot"].std()
plt.figure(figsize=(10, 5))
plt.plot(std_pagos.index, std_pagos.values, marker='o', linestyle='-', color='red')
plt.xlabel("Fecha")
plt.ylabel("Desviación Estándar de Pagos")
plt.title("Desviación Estándar de Pagos respecto al Tiempo")
plt.xticks(rotation=45)
plt.show()

# 5. Cuanto es la deuda total de los clientes
deuda_tot = df["adeudo_actual"].sum()
print('La deuda total de los clientes es:', deuda_tot)

# 6. Cuanto es el porcentaje de utilidad del comercio a partir de el total de las ventas respecto del adeudo 
utilidad = ventas_tot - deuda_tot
porcentaje_utilidad = (utilidad / ventas_tot) * 100 if ventas_tot > 0 else 0
print('El porcentaje de utilidad del comercio es:', round(porcentaje_utilidad, 2), '%')

# 7. Crear un grafico circular de ventas por sucursal.
ventas_sucursal = df.groupby("suc")["ventas_tot"].sum()
plt.figure(figsize=(8, 8))
plt.pie(ventas_sucursal, labels=ventas_sucursal.index, autopct='%1.1f%%', startangle=140)
plt.title("Ventas por Sucursal")
plt.show()

# 8. Presentar un grafico de cuales son las deudas totales por cada sucursal respecto del margen de utilidad de cada sucursal.
fig, ax = plt.subplots(figsize=(10, 5))
deudas_sucursal = df.groupby("suc")["adeudo_actual"].sum()
ax.bar(deudas_sucursal.index, deudas_sucursal.values, color='orange', label='Deuda Total')
ax.set_xlabel("Sucursal")
ax.set_ylabel("Deuda Total")
ax.set_title("Deudas Totales por Sucursal vs Margen de Utilidad")
plt.xticks(rotation=45)
plt.legend()
plt.show()




