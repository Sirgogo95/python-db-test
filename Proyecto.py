import mysql.connector
import Personal_MySQL_Functions as psql
from datetime import datetime



class Proyecto():
    def __init__(self, nombre="", cliente= "", fecha = "2023-03-14", tasa = 56.0, itbis = 18.0, manejo = 10.0, auxiliares = 5.0,desperdicios = 3.0, listados_precios = {}, presupuestos = {}):
        if psql.Database_Exist(nombre) == True: 
            psql.Insert_Proyecto_Table(nombre,cliente,fecha,tasa,itbis,manejo,auxiliares,desperdicios)
        else:
            psql.Create_DB(nombre)
            psql.Create_Proyecto_Table(nombre)
            psql.Insert_Proyecto_Table(nombre,cliente,fecha,tasa,itbis,manejo,auxiliares,desperdicios)
            



x = Proyecto("SCT")