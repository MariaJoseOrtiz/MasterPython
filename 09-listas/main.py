"""
listas: son colecciones de datos bajo un unico nombre , y para acceder esos nombres
se utiliza un indice numerico 
"""

pelicula = "Batman"
#print(pelicula)
#definir lista
peliculas = [ "barman","spiderman", "El senor de los anillos"]
cantantes= list(("2pac","Drake","Dualipa")) #transforma una tupla a lista
year = list(range(2020,2040))
variable = ["maria",20,5.6,True]
"""
print(peliculas)
print(cantantes)
print(year)
print(variable)
"""
#indices 
peliculas[1]= "Gran Torino "
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:1]) # imprime de tal a tal
print(peliculas[1:])# del 1 a todos

#anadir elementos a la lista

cantantes.append("Kase O")
print(cantantes)

#recorrer lista
"""
nueva=""
while(nueva != "parar"):
    nueva= input("introduce tu pelicula")
    if nueva != "parar":
        peliculas.append(nueva)
print("\n###########Listado##############")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}.{pelicula}")
"""
#lista multidimencionales
print("\n ########Lista de contactos#######")

contactos = [

    ['antonio','antonio.com'],
    ["luis", "luis.com"],
    ["salvador","salvador.com"]
]

print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:   
            print("Nombre: " + elemento)
        else:
            print("Email:"+ elemento)
    print("\n")