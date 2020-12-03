# Importar modulo

import sqlite3

#conexion
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()
#Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varvhar(255),
    descripcion text,
    precio int(255)
)""")
# Guardar cambios
conexion.commit()

# insertar datos

cursor.execute("INSERT INTO productos VALUES(Null,'primer_producto','descripcion',550)")
conexion.commit()

# Borrar registro

cursor.execute("DELETE FROM productos")
conexion.commit()

#insertar muchos registros de golpe
productos=[
    
    ("Ordenador portatil", "Buen PC",700),
    ("Telefono movil", "Buen telefono",140),
    ("Placa base", "Buen placa",80),
    ("tablet 15", "Buen tablet",300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit()
# update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")
#listar datos

cursor.execute("SELECT * FROM productos WHERE precio >= 300;")

productos= cursor.fetchall() #para poder ver la tabla en la terminarl
#cerrar conexion
conexion.close()

for producto in productos:
    print("id:",producto[0])
    print("titulo:",producto[1])
    print("Descripcion:",producto[2])
    print("Precio:",producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone() #primero  de la tabla
print(producto)
