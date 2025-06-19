import ast
import json

from dal.usuarios import Usuarios
from models.dataUsuarioLoginRequest import DataUsuarioLoginRequest

data = '{"usuario":"fabiana.preciosa@gmail.com","clave":"","equipoID":"","aplicacionID":""}'
cls = json.loads(data)
obj = DataUsuarioLoginRequest()
obj.usuario = cls["usuario"]
obj.clave = cls["clave"]
print(obj)