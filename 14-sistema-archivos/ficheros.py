from io import open
import pathlib
import shutil

#Abrir archivo
ruta=str(pathlib.Path().absolute()) +"/fichero_texto.txt"
archivo = open(ruta,"a+")
#escribir

archivo.write("Soy un texto metido en python \n")

#cerrar archivo siempre cerrarlo
archivo.close()

#Abrir archivo
ruta=str(pathlib.Path().absolute()) +"/fichero_texto.txt"
archivo_lectura=open(ruta,"r")#lectura

#leer contenido
contenido = archivo_lectura.read()

#print(contenido)

#leer conteid y guardarlo en lista

lista=archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    print("- "+frase)

#copiar
"""
ruta_original= str(pathlib.Path().absolute()) +"/fichero_texto.txt"
ruta_nueva= str(pathlib.Path().absolute()) +"/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) +"/../07-Ejercicios/fichero_copiado88.txt"
shutil.copyfile(ruta_original,ruta_nueva)
"""
#mover 
"""
ruta_original= str(pathlib.Path().absolute()) +"/fichero_copiado.txt"
ruta_nueva=str(pathlib.Path().absolute()) +"/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)
"""
#Eliminar
'''
import os
ruta_nueva=str(pathlib.Path().absolute()) +"/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
'''
#comprobar

import os.path

print(os.path.abspath("../"))

if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print("existe")
else:
    print("no existe")