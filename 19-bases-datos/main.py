import mysql.connector

#conexion

database = mysql.connector.connect(

    host= "localhost",
    user= "root",
    passwd= "1234",

)
#como saber si se realizo correctamente?
# print(database) imprime un objeto mysql

cursor= database.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)