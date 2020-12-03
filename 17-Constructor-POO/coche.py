class Coche:

    #Atributos o propiedades (Caracteristicas del coche)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2
    soyPublico = "Hola soy publico"
    __soyPrivado = "hola soy privado"
    #constructor
    def __init__(self,color, marca,modelo,velocidad,caballaje,plazas):
        
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje =caballaje
        self.plazas =plazas
        
    #metodos, acciones que hace el objeto
    def getPrivado(self):
        return self.__soyPrivado

    def setColor(self,color):
        self.color= color

    def getColor(self):
        return self.color

    def setModelo(self,modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self,marca):
        self.marca=marca

    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad +=1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "--Info del coche--"
        info+= " \n Color: "+self.getColor()
        info += "\n Marca: "+self.getMarca()
        info+= "\n Velocidad: "+str(self.getVelocidad())

        return info 