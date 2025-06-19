import os
import pyodbc

from dotenv import load_dotenv, dotenv_values

class BD_Conn:

    def __init__(self):
        load_dotenv()
        self.BD_DRIVER = os.getenv("BD_DRIVER")
        self.BD_SERVER = os.getenv("BD_SERVER")
        self.BD_DATABASE = os.getenv("BD_DATABASE")
        self.BD_USER = os.getenv("BD_USER")
        self.BD_PASSWORD = os.getenv("BD_PASSWORD")

        self.connection_string = (
            f"DRIVER={{{self.BD_DRIVER}}};"
            f"SERVER={self.BD_SERVER};"
            f"DATABASE={self.BD_DATABASE};"
            f"UID={self.BD_USER};"
            f"PWD={self.BD_PASSWORD};"
            "TRUSTSERVERCERTIFICATE=YES;"
        )
    
    def listar(query: str):
        items = []
        try:
            bd_conn = BD_Conn()
            conn = pyodbc.connect(bd_conn.connection_string)
            cursor = conn.cursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                items.append(row)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == 'HYT00':
                print("Error de tiempo de espera de conexión.")
            else:
                print("Error: ", ex)
            return None
        finally:
            if conn:
                conn.close()
        return items
    
    
    def ejecutar(query: str):
        try:
            bd_conn = BD_Conn()
            conn = pyodbc.connect(bd_conn.connection_string)
            cursor = conn.cursor()
            cursor.execute(query)
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == 'HYT00':
                print("Error de tiempo de espera de conexión.")
            else:
                print("Error: ", ex)
        finally:
            if conn:
                conn.close()