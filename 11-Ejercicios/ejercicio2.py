"""
Ejercicio 2. escribir un programa que a;ada valores a una lista mientras su longitud sea 
menor a 120 y luego mostrar la lista
usar while y for
"""
coleccion = []

#for contador in range(0,120):
    #coleccion.append(f"elemento: {contador}")
    #print(f"mostrando el {coleccion[contador]}")

#print(coleccion[115])

x=0
while x<120:
    coleccion.append(f"elemento - {x}")
    print("ostrando el : "+ coleccion[x])
    x+=1

print(coleccion[77])
