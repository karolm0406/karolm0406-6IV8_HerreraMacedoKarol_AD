import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
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

# Mediana de median_house_value
medianavalor = df["median_house_value"].median()
print('La mediana de median_house_value es:', medianavalor)

# Moda de median_house_value
modavalor = df["median_house_value"].mode()[0]
print('La moda de median_house_value es:', modavalor)

# Rango de median_house_value
rangovalor = df["median_house_value"].max() - df["median_house_value"].min()
print('El rango de median_house_value es:', rangovalor)

# Varianza de median_house_value
varianzavalor = df["median_house_value"].var()
print('La varianza de median_house_value es:', varianzavalor)

# Desviación estándar de median_house_value
desviacionvalor = df["median_house_value"].std()
print('La desviación estándar de median_house_value es:', desviacionvalor)

# Tabla de frecuencias de median_house_value (solo las primeras 10 filas)
tabla_frecuencia = df["median_house_value"].value_counts().head(10)
print("Tabla de frecuencia de median_house_value:")
print(tabla_frecuencia)

# Graficar un histograma de median_house_value
plt.hist(df["median_house_value"], bins=30, color="blue", edgecolor="black")
plt.xlabel("Valor de la Casa (median_house_value)")
plt.ylabel("Frecuencia")
plt.title("Histograma de median_house_value")
plt.show()

# Graficar la comparación entre total_bedrooms y population respecto a median_house_value
plt.scatter(df["total_bedrooms"][:50], df["median_house_value"][:50], color="red", label="Total Bedrooms")
plt.scatter(df["population"][:50], df["median_house_value"][:50], color="green", label="Population")
plt.xlabel("Cantidad")
plt.ylabel("median_house_value")
plt.title("Comparación de total_bedrooms y population con median_house_value")
plt.legend()
plt.show()

