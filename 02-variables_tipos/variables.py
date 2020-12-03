"""
Una vatiables es un contenedor de informacion que dentro guardara
un dato, se pueden crear muchas variables y que cada una tenga un dato distinto.
"""

#crear variables y asignarles un valor
texto= "Master en python"
numero = 45
decimal= 6.7

print(texto)
print(numero)
print(decimal)

print("------------------------------------")

#reasignar valores 
numero= 77
decimal= 4.7

print(numero)
print(decimal)

print("------------------------------------")

#Concatenacion

nombre= 'Maria'
apellido='Ortiz'
web= 'ortizmaria.es'

print(nombre +" "+ apellido + ' - '+ web )
print(f"{nombre} {apellido} - {web}") # recomendable
print("hola me llamo {} {}  y mi web es: {}".format(nombre,apellido,web))
print(nombre,apellido,web)