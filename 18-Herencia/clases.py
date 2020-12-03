#Herencia es la posiblididad de compartir atributos y metodos

class Persona:
    '''
    nombre
    apellido
    altura
    edad
    '''
    def getnombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad   

    def setNombre(self,nombre):
        self.nombre=nombre

    def getNombre(self):
        return self.nombre
    def setApellido(self,apellido):
        self.apellido = apellido

    def setAltura(self,altura):
        self.altura = altura

    def setEdad(self,edad):
        self.edad = edad   

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):

    """
    lenguaje
    experiencia
    """
    def __init__(self):
        self.lenguajes = "HTML,CSS,JavaScript,PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self,lenguajes):
        self.lenguajes= lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "Estoy reparando la pc"
    
class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__()
        self.auditarRedes ="experto"
        self.experienciaRedes = 15
        
    def auditoria(self):
        return "Estoy auditando"
