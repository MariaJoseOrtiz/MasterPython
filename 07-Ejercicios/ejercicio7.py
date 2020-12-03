"""
Ejercicio 7. 
Hacer un programa que muestre todos los numeros impares
enre dos numero que decida el usuario
"""

numero1 = int(input("Introduzca el primer numero: "))
numero2= int(input("Introduzca el segundo numero: "))

if(numero1 < numero2):

    for contador in range(numero1,numero2+1):
        if contador % 2 == 0:
            print(f"Es par{contador}")
        else:
            print(f"Es impar{contador}")
else:
    print("Tiene que ser numero 1 menor al 2")