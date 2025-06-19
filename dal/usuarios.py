from dal.bd_conn import BD_Conn

class Usuarios:
    def __init__(self):
        return True

    def listar_usuarios():
        items = BD_Conn.listar(f"SELECT * FROM XDTR WHERE VAHDHA=1")
        return items


    def listar_trabajadores(id_asociado: int):
        items = BD_Conn.listar(f"SELECT * FROM XDTR WHERE VAHDHA=1 AND TISODI={id_asociado}")
        return items


    def datos_usuario(usuario: str):
        query = f"SELECT * FROM XDTR WHERE VAHDHA=1 AND MABIDO='{usuario}'"
        items = BD_Conn.listar(query)
        return items