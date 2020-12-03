# programacion orientada a objetos
#definir una clase
#molde para crear objetos de ese tipo
#coche

class Coche:

    #Atributos o propiedades (Caracteristicas del coche)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #metodos, acciones que hace el objeto
    def setColor(self,color):
        self.color= color

    def getColor(self):
        return self.color

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
# fin definicion de clase

#crear objeto
coche = Coche()

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print(coche.marca,coche.getModelo(),coche.getColor())

print("Velocidad actual: " + str(coche.getVelocidad()) )
coche.acelerar()
coche.acelerar()
coche.frenar()
print("Velocidad actual: " + str(coche.getVelocidad()) )


#crear mas objeto

coche2=Coche()
print("--------------------------------------")
print("Coche 2: ")

coche2.setColor("verde")
coche2.setModelo("Gallardo")
print(coche2.getColor())
print(coche2.marca,coche2.getModelo(),coche2.getColor())

