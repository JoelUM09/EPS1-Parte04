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
    opcion=int(input("Digite la opcion que desea: "))
    if opcion==1:
        registrar()
    elif opcion==4:
        listar()

def listar():
    conexion=sqlite3.connect("SAIRA_almacen.db")
    cursor=conexion.cursor()
    consulta="""SELECT * FROM producto
                """
    cursor.execute(consulta)
    records = cursor.fetchall()
    print("Total de productos registrados:  ", len(records))
    print("Esta es la lista de productos")
    for row in records:
        print("Id: ", row[0])
        print("Codigo: ", row[1])
        print("Nombre: ",row[2])
        print("Precio: ",row[3])
        print("\n")
    conexion.commit()
    conexion.close()

def registrar():
    conexion=sqlite3.connect("SAIRA_almacen.db")
    print("Ingrese los siguientes datos")
    nombre=input("Digite el nombre del Producto: ")
    codigo=input("Digite el codigo del producto: ")
    precio=float(input("Digite el precio del producto:"))
    conexion.execute("insert into producto(codigo,nombre,precio) values (?,?,?)", (codigo,nombre,precio))
    conexion.commit()
    conexion.close()
    
menu()