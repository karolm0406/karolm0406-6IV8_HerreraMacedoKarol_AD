import numpy as np
import pandas as pd
from scipy.spatial import distance

# Definimos las coordenadas de las tiendas
puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1),
}

# Convertir las coordenadas a un DataFrame para facilitar el cálculo
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print("Coordenadas de los puntos")
print(df_puntos)

def calcular_distancias(df_puntos, tipo):
    distancias = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i != j:
                if tipo == "euclidiana":
                    distancias.loc[i, j] = round(distance.euclidean(df_puntos.loc[i], df_puntos.loc[j]), 2)
                elif tipo == "manhattan":
                    distancias.loc[i, j] = round(distance.cityblock(df_puntos.loc[i], df_puntos.loc[j]), 2)
                elif tipo == "chebyshev":
                    distancias.loc[i, j] = round(distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j]), 2)
    return distancias

# Calcular distancias con cada métrica
distancias_euclidiana = calcular_distancias(df_puntos, "euclidiana")
distancias_manhattan = calcular_distancias(df_puntos, "manhattan")
distancias_chebyshev = calcular_distancias(df_puntos, "chebyshev")

print("\nTabla de distancias Euclidiana")
print(distancias_euclidiana)
print("\nTabla de distancias Manhattan")
print(distancias_manhattan)
print("\nTabla de distancias Chebyshev")
print(distancias_chebyshev)

# Encontrar la distancia máxima para cada tipo de métrica
max_euclidiana = distancias_euclidiana.max().max()
max_manhattan = distancias_manhattan.max().max()
max_chebyshev = distancias_chebyshev.max().max()

print("\nDistancia máxima Euclidiana:", max_euclidiana)
print("Distancia máxima Manhattan:", max_manhattan)
print("Distancia máxima Chebyshev:", max_chebyshev)

