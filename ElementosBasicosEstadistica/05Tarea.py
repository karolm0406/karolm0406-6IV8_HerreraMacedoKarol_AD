import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo XLSX
df = pd.read_excel('ElementosBasicosEstadistica/Dato_Con_Sucursal.xlsx')

#total de las ventas 
ventas_tot = df["ventas_tot"].sum()
print('La suma de las ventas totales  es:', ventas_tot)

#personas que tienen adeudo
tot_adeudo = df[""]
print('la cantidad de socios que tienen adeudo son')

#personas que no tienen adeudo
tot_no_adeudo = df[""]
print('la cantidad de socios que no tienen adeudo son')



