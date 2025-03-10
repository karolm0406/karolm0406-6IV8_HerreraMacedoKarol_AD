import pandas as pd
##escribir un programa que pregunte al ususario por las ventas de un rango de años y muestre en la pantalla una serie de datos de ventas idexadas po los años, antes y despues de aplicarles un descuento.

inicio = int(input('introduce el año de ventas inicial: ')) 
fin= int(input('introduce el año final de ventas: '))

ventas={}

for i in range (inicio, fin+1):
    ventas[i] = float(input('introduce las ventas del alo: ' + str(i) + ': ' ))
ventas = pd.Series(ventas)
print('Ventas \n', ventas)
print('ventas con descuento \n', ventas*0.9)