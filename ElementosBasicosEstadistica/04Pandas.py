import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('ElementosBasicosEstadistica/housing.csv')

#mostrar las 1eras 5 filas
print(df.head())

#mostar las ultimas 5 filas
print(df.tail())

#mostar una fila en especifico
print(df.iloc[7])

#mostar la columna  ocean_proximity
print(df["ocean_proximity"])

#obtener la media de la coluna total_rooms
mediadecuarto = df["total_rooms"].mean()
print('la media de total room es: ', mediadecuarto)

#mediana
medianacuarto = df ['median_house_value'].median()
print('la mediana de la columna valor mediana de la casa: ', medianacuarto)

#la suma de popular
salariototal = df['population'].sum()
print('el saario total es de: ', salariototal)

#para poder filtrar 
vamoshacerunfiltro = df[df['ocean_proximity'] == 'ISLAND']
print(vamoshacerunfiltro)


#vamos a hacer un grafico de dispersion
plt.scatter(df['ocean_proximity'][:10], df['median_house_value'][:10])
#nombramos lpos ejes
plt.xlabel("Proximidad")
plt.ylabel("Precio")

plt.title("grafico de dispersion de proximida de al oceano vs precio")
plt.show()
