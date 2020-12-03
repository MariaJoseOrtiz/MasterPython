"""
Variable local: se definen dentro de la funcion y no se puede usar fuera de ella,
solo estan disponibles dentro. a no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion y estan disponibles dentro 
y fuera de ellas.
"""
#variable global

frase= "Hola maria"

print(frase)

def holaMundo():
    frase="Hola Mundo"
    print("Dentro de la funcion:")
    print(frase)

    year=2021
    print(year)

    global website  
    """si se declara global se puede usar la variable tanto fuera
    como dentro de la funcion"""
    website = 'maria.es'
    print("Dentro:", website)

    return "Dato devuelto "+str(year)

print(holaMundo())
print("fuera: ", website)