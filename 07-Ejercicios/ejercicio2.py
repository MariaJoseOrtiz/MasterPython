"""
Ejericio 2
Escribir un script que nos muestre por pantalla todos los numeros pares del 1 al 120 
"""

numero = 1
# con while
while numero <=120:
    numero_par = numero % 2
    if numero_par == 0 :
        print(numero) 
    numero+=1

# con for 
for contador in range(1,121):
    if contador % 2 == 0:
        print(contador)