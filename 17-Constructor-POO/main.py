from coche import Coche

carro = Coche("Amarillo","Renault","Clio",150,200,4)
carro1 = Coche("Verde","Sear","Psanda",140,200,4)
carro2 = Coche("Azul","Citroen","Xara",180,200,4)

print(carro.getColor())

print(carro.getInfo())
print(carro2.getInfo())
print(carro1.getInfo())

#Detectar tipo

if type(carro)==Coche:
    print("es de tipo carro")
else:
    print(" no es de tipo carro")

#visibilidad
print(carro.soyPublico)
print(carro.getPrivado())