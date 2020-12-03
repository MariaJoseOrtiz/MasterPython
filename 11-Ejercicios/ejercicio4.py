"""
ejercicio 4. crear un script que tenga 4 variables, una lista, un string, un 
entero y un booleano y que imprima un mensaje
segun el tipo de dato de cada variable.usar funciones
"""

mi_lista = ["hola mundo", 77]

titulo = "Mastes en Pyton"
numero = 100

verdadero= True

def comprobarTipado(dato,tipo):
    test= isinstance(dato,tipo)
    result = ""
    if test:
        result = f"Este dato es del tipo {type(dato)}"
    else:
        result= None

    return result

print(comprobarTipado(mi_lista, list))

