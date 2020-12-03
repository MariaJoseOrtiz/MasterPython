"""
Ejericico 6
Mostrar todas las tablas de multiplicar del 1 al 10 , 
mostrando el titulo de la multiplicacion y luego las multiplicaciones
"""

numero = 1

while numero <= 10:
    print(f"###Tabla del {numero}###")
    for contador in range(1,11):
        print(f"{numero} x {contador} = {numero * contador}") 
    numero += 1
    print("\n")