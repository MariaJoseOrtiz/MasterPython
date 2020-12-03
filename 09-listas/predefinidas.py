cantantes = ["2pac","Drake","Bad bony"]

numeros= [1,2,5,8,3,4]

#ordenar una lista 
print(numeros)

numeros.sort()
print(numeros)

#Anadir elementos
cantantes.append("Dualipa")
print(cantantes)
#Anadir en un indice especifico 
cantantes.insert(1,"David Bisval")
print(cantantes)

#Eliminar elementos 
cantantes.pop(1)
cantantes.remove("Drake")
print(cantantes)

#dar la vuela, el iniicio es el fin y el fin es el inicio jaajaj 
numeros.reverse()
# Buscar dentro de una lista
print("Bad bony" in cantantes)

#contar
print(len(cantantes))

#cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#conseguir un indice

print(cantantes.index("Bad bony"))

#unir listas
cantantes.extend(numeros)
print(cantantes)

