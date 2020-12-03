"""
Ejericio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
Recorrer la lista y mortarla
hacer una funcion que recorra lista y devuelva un string
Ordenarla y mostrarla
Mostrar su longitud
Buscar algun elemento que el usuario pida por teclado 
"""

# crear list
numeros= [13,64,52,73,21,99,4]
def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado +="Elemento "+str(elemento)
        resultado += "\n"
    return resultado

#recorrer y mostrar
print("#########Recorrer y mostrar####")
for numero in numeros:
    print(numero )

print(mostrarLista(numeros))

#ordenar lista
numeros.sort()
print(f"lista ordenada {numeros}")

#mostrar longitud
print(len(numeros))

#busqueda en la lista
try:
    busqueda =int( input("dame numero: "))
    comprobar = isinstance(busqueda, int)

    while not comprobar or busqueda <= 0:
        busqueda = int(print("nmero: "))
    else:
        print(f"has introducido {busqueda}")
    search= numeros.index(busqueda)
    print(f"El numero buscado existe en la lista")

except:
    print("El numero no esta en la lista, sorry")