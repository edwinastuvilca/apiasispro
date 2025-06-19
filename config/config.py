import pyodbc

# Sustituye los valores por los de tu base de datos
driver = 'ALM0001.mssql.somee.com'
server = 'ALM0001.mssql.somee.com'
database = 'ALM0001'
user = 'desarrollo'
password = 'desarrollo2006'

# Cadena de conexión
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};TRUSTSERVERCERTIFICATE=YES;"
# connection_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};TRUSTSERVERCERTIFICATE=YES;"
# connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};TRUSTSERVERCERTIFICATE=YES;"
# connection_string = "workstation id=ALM0001.mssql.somee.com;packet size=4096;user id=desarrollo;pwd=desarrollo2006;data source=ALM0001.mssql.somee.com;persist security info=False;initial catalog=ALM0001;TrustServerCertificate=True"

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=d_BD001;"
    "UID=desarrollo;"
    "PASSWORD=desarrollo2006;"
    "charset=utf8mb4;"
)

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server},49242;"
    "SERVER=ALM0001.mssql.somee.com;"
    "DATABASE=ALM0001;"
    "UID=desarrollo;"
    "PWD=desarrollo2006;"
    #"TrustServerCertificate=yes;"
)

connection_string  = (
    "DRIVER={CData ODBC Driver for MySQL};"
    "SERVER=localhost;"
    "DATABASE=d_BD001;"
    "UID=desarrollo;"
    "PASSWORD=desarrollo2006;"
)

# cnxn = pyodbc.connect("DRIVER={MySQL ODBC 3.51 Driver}; SERVER=localhost;DATABASE=mydb; UID=root; PASSWORD=thatwouldbetelling;") 

try:
    connection_string = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};TRUSTSERVERCERTIFICATE=YES;"

    # Conectar a SQL Server
    conn = pyodbc.connect(connection_string)
    print("Conexión exitosa a SQL Server")

    # Crear un cursor
    cursor = conn.cursor()

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM XDTR")
    for row in cursor.fetchall():
        print(row)

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    if sqlstate == 'HYT00':
        print("Error de tiempo de espera de conexión.")
    else:
        print("Error: ", ex)
finally:
    # Cerrar la conexión
    # if conn:
    # conn.close()
    print("Conexión cerrada.")