import mysql.connector


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
        if str(name).lower() == _[0]:
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
