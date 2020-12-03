"""
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto
que puede reutilizarse invocando a la funcion tantas veces como sea necesario

def nombreDeLaFuncion(parametros):
    bloque de instrucciones

nombreFuncion(parametro)
"""

print("###EJEMPLO !######")

# Crea funcion
def muestraNombre():
    print("Maria")
    print("Cesar")
    print("Juan")
    print("\n")

#invocar funcion
muestraNombre()

print("###EJEMPLO 2 !######")

nombre = "maria"
#input("Introduce tu nombre: ")

def mostrarTuNombre(nombre):
    print(f"Tu nombre es: {nombre} ")

mostrarTuNombre(nombre)

print("###EJEMPLO 3 !######")

def tablaMultipicar(numero):
    print(f"Tabla de multiplicar del numero: {numero}")
    for contador in range(0,11):
        operacion = numero * contador
        print(f"{numero} X {contador}={operacion}")

    print("\n")

tablaMultipicar(3)

print("###EJEMPLO 4 !######")

#parametros opcionales
#cedula es un parametro por defecto
def getEmpleado(nombre,cedula = None):
    print("Empleado")
    print(f"Nombre: {nombre}")

    if cedula != None:
        print(f"cedula: {cedula}")

getEmpleado("Maria")

print("###EJEMPLO 5 !######")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

print(saludame("Victor Robles"))

#Ejemplo 6
print("###EJEMPLO 6 !######")

def calculadora(numero1,numero2,basico = False):
    suma= numero1+numero2
    resta= numero1-numero2
    multi= numero1*numero2
    division= numero1/numero2
    cadena =""
    if basico != False:
        cadena+= "Suma:"+str(suma)
        cadena += "\n"
        cadena+="Resta:"+str(resta)
        cadena += "\n"
    else:
        cadena+="Multi:"+str(multi)
        cadena += "\n"
        cadena+= "Divicion:"+str(division)

    return cadena

print(calculadora(5,4))

print("###EJEMPLO 7 !######")
#funciones dentro de funciones
def getNombre(nombre):
    texto= f"El nombre es {nombre}"
    return texto
def getApellido(apellido):
    texto=f"El apellido es {apellido}"
    return texto
def devuelveNombre(nombre,apellido):
    texto= getNombre(nombre)+ "\n"+getApellido(apellido)
    return texto

print(devuelveNombre("Maria","ortiz"))

print("###EJEMPLO 8 !######")
#funciones lambda
# son funciones que se utilizan para codigo de una linea , corticas
dime_el_year= lambda year: f"El ano es {year*50}"

print(dime_el_year(2020))