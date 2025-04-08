import numpy as np
import pandas as pd
from scipy.spatial import distance

# Definimos las coordenadas de los puntos
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

#calcular las distancias
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
            else:
                distancias.loc[i, j] = 0.0
    return distancias

#encontrar pares más cercanos y más lejanos
def obtener_pares_extremos(distancias):
    dist_copia = distancias.replace(0, np.nan)
    min_val = dist_copia.min().min()
    max_val = dist_copia.max().max()
    par_min = dist_copia[dist_copia == min_val].stack().index[0]
    par_max = dist_copia[dist_copia == max_val].stack().index[0]
    return par_min, min_val, par_max, max_val

#distancias 
distancias_euclidiana = calcular_distancias(df_puntos, "euclidiana")
distancias_manhattan = calcular_distancias(df_puntos, "manhattan")
distancias_chebyshev = calcular_distancias(df_puntos, "chebyshev")


print("\nTabla de distancias Euclidiana")
print(distancias_euclidiana)
print("\nTabla de distancias Manhattan")
print(distancias_manhattan)
print("\nTabla de distancias Chebyshev")
print(distancias_chebyshev)

# Mostrar pares más cercanos y más lejanos
for nombre, matriz in [("Euclidiana", distancias_euclidiana), ("Manhattan", distancias_manhattan), ("Chebyshev", distancias_chebyshev)]:
    par_min, min_val, par_max, max_val = obtener_pares_extremos(matriz)
    print(f"\nMétrica {nombre}:")
    print(f"Par más cercano: {par_min[0]} y {par_min[1]} con distancia {min_val}")
    print(f"Par más lejano: {par_max[0]} y {par_max[1]} con distancia {max_val}")


