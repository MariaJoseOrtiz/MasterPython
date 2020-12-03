"""
for 
for variables in elemento_iterable (lista, rango, tupla, etc)
    Bloque de instrucciones
"""
contador = 0
resultado = 0 

for contador in range(0,10):
    print("voy por el "+ str(contador))
    resultado = resultado + contador

print(f"El resultado es {resultado}")

#tabla de multiplicar
print("\n ################EJEMPLO####################")

numero_usuario= int(input("De que numero quieres la tabla"))

if numero_usuario < 1:
    numero_usuario= 1

print(f"### tabla de multiplicar del numero {numero_usuario}####")

for numero_tabla in range(1,11):
    
    if numero_usuario == 45 :
        print("no se puede mostrar numero prohibidos!!")
        break # cortar el bucle

    print(f"{numero_usuario} x {numero_tabla}={numero_usuario*numero_tabla}")
else: # cuando termina todo el for imprime mensaje
    print("tabla finalizada ")