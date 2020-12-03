"""
Diccionario es un tipo de datos que almacena un conjunto de datos,
en dorma de clave valor
"""

persona={

    "nobre": "Maria",
    "Apellido": "Ortiz",
    "web":"maria.es"
}
#print(persona["Apellido"])

#Lista con diccionarios

contactos = [
    {
        "nombre":"Maria",
        "email":"maria@gmail.com",
        "apellido": "Ortiz",
        "web":"maria.es",
    },
    {
        "nombre":"Cesar",
        "email":"Cesar@gmail.com"
    },
    {
        "nombre":"Pepe",
        "email":"pepe@gmail.com"

    }     

]
contactos[0]['nombre']="antonio"
print(contactos[0]['nombre'])

print("\n Listado de contactos")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']} ")
    print(f"Email del contacto: {contacto['email']}")
    print("---------------------------------------")