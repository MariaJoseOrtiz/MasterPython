"""
son funcionalidades ya hechas para reutilizar
en python puedes consultar 
podemos conseguir modulos que ya vienen en el lenguaje
podemos crear modulos


# importar modulo propio
import mimodulo
print(mimodulo.calculadora(1,3,True))

#importando solo una funcion de mi modulo
from mimodulo import holaMundo
print(holaMundo("maria"))

#importando todas las funciones 
from mimodulo import * 

"""

#modulo de fecha
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y")

print(fecha_personalizada)

# modulo matematicas

import math

print("Raiz cuadrada de 10:",math.sqrt(10))

print("numero pi: ", math.pi)

print("redondear: ", math.floor(6.7777788))

#modulo random

import random

print("numero aleatorio este 15 y 67 ", random.randint(15,67))