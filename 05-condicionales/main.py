
# condicional if
print("########### Ejemplo 1 ################")

color="verde"

#color = input("Adivina cual es mi color favorito?: ")

if color == "rojo":
    print("Adivinaste!!!")
    print("El color es rojo")
else:
    print("Color incorrecto")

# operadores de comparacion 
"""
== igual 
!= diferente
<menor
> mayor
<= menor igual
>= mayor igual
"""
print("########### Ejemplo 2 ################")

ano = 2020
#ano = int(input("En que ano estamos?: "))

if ano >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un ano anterior a 2021")

# if anidados

print("########### Ejemplo 3 ################")

nombre= "Maria"
ciudad = "Caracas"
pais= "Venezuela"
edad= 26
mayoria_edad= 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!!")
    if  pais != "Venezuela":
        print("El usuario NO es Venezolano")
    else:
        print(f"Es Venezolano y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")


print("########### Ejemplo 4 ################")
"""
dia = int(input("Introduce el dia de la semana: "))

if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia ==4:
                print("Es jueves")
            else:
                if dia == 5:
                    print ("Es Viernes")
                else:
                    print("Es fin de semana ")
"""
#Elif 
#dia = int(input("Introduce el dia de la semana: "))
dia = 2
if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es fin de semana ")

#Ejemplo 5
print("########### Ejemplo 5 ################")

edad_minima = 18 
edad_maxima=65
#edad_oficial=int(input("Que edad tienes?: "))
edad_oficial= 17
if edad_oficial >=18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

# operadores logicos
"""
or o
and y
! negacion
not NO
"""
print("########### Ejemplo 6 ################")

pais= "Alemania"
if (pais == "Mexico" or pais == "Espana" or pais=="Colombia"):
    print(f"{pais} es un pais de habla hispana")
else: 
    print(f"{pais} no es de habla hispana ")

print("########### Ejemplo 7 ################")

pais= "Espana"

if not (pais == "Mexico" or pais == "Espana" or pais=="Colombia"): # que no se cumpla algo
    print(f"{pais} NO es un pais de habla hispana")
else: 
    print(f"{pais} SI es de habla hispana ")


print("########### Ejemplo 8 ################")

pais= "Colombia"

if (pais != "Mexico" or pais != "Espana" or pais!="Colombia"): # que no se cumpla algo
    print(f"{pais} NO es un pais de habla hispana")
else: 
    print(f"{pais} SI es de habla hispana ")