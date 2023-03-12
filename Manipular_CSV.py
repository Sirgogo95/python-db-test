import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database='mydatabase'
    )

mycursor = mydb.cursor()


def Agregar_Materiales_CSV():

    data = pd.read_csv(R"C:\Users\Junior\Desktop\GitHub\Materiales.csv", encoding = "ISO-8859-1")   
    df = pd.DataFrame(data)

    op = "INSERT INTO mydatabase.material (Codigo, Familias, Nombre, Alias, Tasa, Unidad) VALUES (%s, %s ,%s, %s, %s, %s)"

    for row in df.itertuples():
        mycursor.execute(op,(row.Codigo, row.Familias, row.Nombre, row.Alias, row.Tasa, row.Unidad))
        
    mydb.commit()



def Agregar_Suplidores_CSV():

    data = pd.read_csv(R"C:\Users\Junior\Desktop\GitHub\Suplidores.csv", encoding = "ISO-8859-1")   
    df = pd.DataFrame(data)

    op = "INSERT INTO mydatabase.suplidores (Suplidor, Telefono, Ubicacion, Correo, Nombre_Vendedor) VALUES (%s, %s ,%s, %s, %s)"

    for row in df.itertuples():
        mycursor.execute(op,(row.Suplidor, row.Telefono, row.Ubicacion, row.Correo, row.Nombre_Vendedor))
        
    mydb.commit()



def Agregar_Precios_CSV():

    data = pd.read_csv(R"C:\Users\Junior\Desktop\GitHub\Precios.csv", encoding = "ISO-8859-1")   
    df = pd.DataFrame(data)

    op = "INSERT INTO mydatabase.precios (Codigo, Suplidor, Fecha, Precio_sin_Itbis, Marca) VALUES (%s, %s ,%s, %s, %s)"

    for row in df.itertuples():
        mycursor.execute(op,(row.Codigo, row.Suplidor, row.Fecha, row.Precio_sin_Itbis, row.Marca))
        
    mydb.commit()





def main():

    Agregar_Precios_CSV()

if __name__ == "__main__":

    main()