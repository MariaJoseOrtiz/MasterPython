import os 
import shutil
#Crear carpeta
"""
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe")
"""
#eliminar
#os.rmdir('./mi_carpeta')

#copiar
"""
ruta_original= "./mi_carpeta"
ruta_nueva= "/mi_carpeta_COPIADA"

shutil.copytree(ruta_original,ruta_nueva)
"""
#eliminar
"""
os.rmdir("./mi_carpeta")
"""
print("contenido de carpeta")
contenido=os.listdir("./mi_carpeta")

for fichero in contenido:
    print("fichero"+ fichero)