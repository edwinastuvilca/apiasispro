import json

from dal.usuarios import Usuarios

from models.dataAplicacionRequest import DataAplicacionRequest
from models.dataUsuarioLoginRequest import DataUsuarioLoginRequest

class Seguridad:
    def validar_version(obj: DataAplicacionRequest):
        return {
            "Version": obj,
            "Tocken": obj.TockenApp
        }
    

    def autenticar(data: DataUsuarioLoginRequest):
        items = []
        rows = Usuarios.datos_usuario(data.usuario)
        # rows = Usuarios.listar_usuarios()
        for item in rows:
            items.append({
                "usuarioID": item.RAJOFI,
                "personaID": item.WALINE,
                "asociadoID": item.TISODI,
                "usuario": item.MABIDO,
            })
        mensajes = [
            {
                "Valor": None,
                "TipoMensaje": None,
                "Mensaje": None,
            }
        ]
        return {
            "RegistroID": items.count,
            "NombrePersona": None,
            "ValorRespuesta": None,
            "RequiereAutenticar": None,
            "ConError": None,
            "Mensajes": mensajes,
        }
