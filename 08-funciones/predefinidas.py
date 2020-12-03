# funciones predefinidas

nombre = "Maria"
# funciones generales
print(type(nombre))

#detectar el tipado
comprobar= isinstance(nombre, str)
if comprobar == str:
    print("Es un string")
else:
    print("no es cadena")
# limpiar espacios
frase= "   mi contenido     "
print(frase)
print(frase.strip())
#eliminar variables
year= 2020
print(year)
del year
#print(year)
#comprobar variables vacias
texto= " ff "
if len(texto)<= 0:
    print("Variable vacia")
else:
    print(len(texto))

#encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))
#remplazar variables
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

# mayusculas y minusculas

print(nombre)
print(nombre.lower()) #minusculas
print(nombre.upper())#mayusculas





