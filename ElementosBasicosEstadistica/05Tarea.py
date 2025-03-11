import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

# media de la columna median_house_value
mediavalor = df["median_house_value"].mean()
print('La media de median_house_value es:', mediavalor)

# Mediana 
medianavalor = df["median_house_value"].median()
print('La mediana es:', medianavalor)

# Moda 
modavalor = df["median_house_value"].mode()[0]
print('La moda  es:', modavalor)

# Rango 
rangovalor = df["median_house_value"].max() - df["median_house_value"].min()
print('El rango  es:', rangovalor)

# Varianza 
varianzavalor = df["median_house_value"].var()
print('La varianza es:', varianzavalor)

# Desviación estándar 
desviacionvalor = df["median_house_value"].std()
print('La desviación estándar es:', desviacionvalor)

# Tabla de frecuencias de solo las primeras 10 filas
tabla_frecuencia = df["median_house_value"].value_counts().head(10)
print("Tabla de frecuencia:")
print(tabla_frecuencia)

# histograma
plt.hist(df["median_house_value"], bins=30, color="blue", edgecolor="black")
plt.xlabel("Valor de la Casa (median_house_value)")
plt.ylabel("Frecuencia")
plt.title("Histograma de median_house_value")
plt.show()

# comparación entre total_bedrooms y population
plt.scatter(df["total_bedrooms"][:50], df["median_house_value"][:50], color="red", label="Total Bedrooms")
plt.scatter(df["population"][:50], df["median_house_value"][:50], color="green", label="Population")
plt.xlabel("Cantidad")
plt.ylabel("median_house_value")
plt.title("Comparación de total_bedrooms y population con median_house_value")
plt.legend()
plt.show()

