"""
Ejericcio  3

Escribir un programa que muestre los cuadrados (un 
numero multiplicado por si mismo ) de los 60 primeros numeros naturales con for y 
while

"""

# while
numero = 0
while numero <=60:
    numero_cuadrado = numero * numero
    print(f"El numero es {numero} y su cuadrado es {numero_cuadrado}")
    numero+=1

# for

for contador in range(0,61):
    numero_cuadrado = contador * contador
    print(f"El numero es {contador}y su cuadrado es {numero_cuadrado}")