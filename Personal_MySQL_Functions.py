import mysql.connector
from datetime import date


def Table_Exist(name,database) -> bool:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database=database
    )

    mycursor = mydb.cursor()

    mycursor.execute("show tables")

    for _ in mycursor:
        if str(name).lower() == str(_[0]).lower():
            mydb.close()
            return True
    return False

def Database_Exist(database) -> bool:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    )

    mycursor = mydb.cursor()

    mycursor.execute("show databases")

    for _ in mycursor:
        if str(database).lower() == str(_[0]).lower():
            mydb.close()
            return True
    return False
    



def Create_DB(name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"create database {name} """)

    mydb.close()



def Create_Proyecto_Table(name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database=name
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"""CREATE TABLE {name} (
                        Nombre VARCHAR(255) NOT NULL,
                        Cliente VARCHAR(255) NULL,
                        Fecha DATE NULL,
                        Tasa FLOAT NULL,
                        Itbis FLOAT NULL,
                        Manejo FLOAT NULL,
                        Auxiliares FLOAT NULL,
                        Desperdicios FLOAT NULL,
                        Listado_Precios VARCHAR(1000) NULL,
                        Presupuestos VARCHAR(1000) NULL,
                        PRIMARY KEY (Nombre))""")
    
    mydb.close()


def Insert_Proyecto_Table(name = "",cliente= "", fecha = "", tasa = 56.0, itbis = 18.0, manejo = 10.0, auxiliares = 5.0,desperdicio = 3.0):
    name = name.lower()
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database=name
    )

    mycursor = mydb.cursor()
    
    op = """INSERT INTO %s.%s (Nombre, Cliente, Fecha, Tasa, Itbis, Manejo, Auxiliares, Desperdicios) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    val = (name,name,name,cliente,fecha,tasa,itbis,manejo,auxiliares,desperdicio)
    mycursor.execute(op,val)

    mydb.commit

    mydb.close()


def main():
    print(Database_Exist("mydatabase"))
  

if __name__ == "__main__":

    main()

