#Capturar execepciones y manejar errores en codigo 
#suseptile a fallos
'''
try:
    nombre= input("Cual es tu nombre?")
    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre
    print(nombre_usuario)
except:
    print("Error Escribe tu nombre ")
else:
    print("todo funciona")
finally:
    print("Fin de la iteracion !! ")
'''
#multiple excepciones
'''
try:
    numero= int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es: "+str(numero*numero))
#except TypeError:
    #print("Debes convertir tus cadenas a enteros")
#except ValueError:
    #print("introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un error:",type(e).__name__)

'''
#Excepciones personalizadas
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("introduce la edad: "))

    if edad< 5 or edad >110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre)<= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al master en pyton {nombre}!!")

except ValueError:
    print("Introduce bien los datos")
except Exception as e:
    print("Existe un error")