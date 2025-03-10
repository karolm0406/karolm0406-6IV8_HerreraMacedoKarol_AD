import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

# Mostrar las primeras 5 filas
print(df.head())

# Mostrar las últimas 5 filas
print(df.tail())

# Mostrar una fila en específico
print(df.iloc[7])

# Mostrar la columna ocean_proximity
print(df["ocean_proximity"])

# Obtener la media de la columna median_house_value
mediavalor = df["median_house_value"].mean()
print('La media de median_house_value es:', mediavalor)

# Mediana 
medianavalor = df["median_house_value"].median()
print('La mediana  es:', medianavalor)

# Moda 
modavalor = df["median_house_value"].mode()[0]
print('La moda  es:', modavalor)

# Rango 
rangovalor = df["median_house_value"].max() - df["median_house_value"].min()
print('El rango es:', rangovalor)

# Varianza
varianzavalor = df["median_house_value"].var()
print('La varianza  es:', varianzavalor)

# Desviación estándar 
desviacionvalor = df["median_house_value"].std()
print('La desviación estándar  es:', desviacionvalor)

# Tabla de frecuencias de las primeras 10 filas
tabla_frecuencia = df["median_house_value"].value_counts().head(10)
print("Tabla de frecuencia de median_house_value:")
print(tabla_frecuencia)

