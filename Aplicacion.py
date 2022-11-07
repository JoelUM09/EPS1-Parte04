import sqlite3
from pathlib import Path
def crear():
    conexion=sqlite3.connect("SAIRA_almacen.db")

    #En una cadena vamos a guardar la creacion del script  de la tabla.
    tabla_producto="""CREATE TABLE producto(
                    idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo TEXT,
                    nombre TEXT,
                    precio FLOAT)
                    """
    #PARA LAS TABLAS
    cursor=conexion.cursor()
    cursor.execute(tabla_producto)
    conexion.close()


def menu():
    if Path("SAIRA_almacen.db").exists()==False:
        crear()  
    print("Menu opciones")
    print("1.Registrar")
    print("2.Eliminar")
    print("3.Editar")
    print("4.Listar")
    print("5.Salir")
    
menu()