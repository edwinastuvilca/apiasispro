import json

from controllers.maestros import Maestros
from controllers.seguridad import Seguridad
from dal.usuarios import Usuarios
from models.dataAplicacionRequest import DataAplicacionRequest
from models.dataUsuarioLoginRequest import DataUsuarioLoginRequest

from fastapi import FastAPI

app = FastAPI()

@app.post("/seguridad/validacionVersion")
def validacionVersion(obj: str):
    # module = importlib.import_module("DataAplicacionRequest")
    cls = json.loads(obj)
    data = DataAplicacionRequest()
    data.TockenApp = cls["TockenApp"]
    data.Version = cls["Version"]
    return Seguridad.validar_version(data)


@app.post("/seguridad/autenticar")
def login(obj: str):
    cls = json.loads(obj)
    data = DataUsuarioLoginRequest()
    data.usuario = cls["usuario"]
    data.clave = cls["clave"]
    data.equipoID = cls["equipoID"]
    data.aplicacionID = cls["aplicacionID"]
    return Seguridad.autenticar(data)


@app.post("/seguridad/crear_usuario")
def crear_usuario():
    return Maestros.crear_usuario()


@app.get("/my-first-api")
def hello(name = None):
    if name is None:
        text = 'Hello!'
    else:
        text = 'Hello ' + name + '!'
    return text


@app.post("/saludar")
def post_saludar(name = None):

    if name is None:
        text = 'Hola!'
    else:
        text = 'Hola ' + name + '!'


@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hello!'
    else:
        text = 'Hello ' + name + '!'
    return text


@app.post("/saludar")
def post_saludar(name = None):

    if name is None:
        text = 'Hola!'
    else:
        text = 'Hola ' + name + '!'
    return text


# @app.get("/get-iris")
# def get_iris():
# 
#     import pandas as pd
#     url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
#     iris = pd.read_csv(url)
# 
#     return iris


# @app.post("/get-iris")
# def post_iris():
# 
#     import pandas as pd
#     url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
#     iris = pd.read_csv(url)
# 
#     return iris
#     return text


# @app.get("/get-iris")
# def get_iris():
# 
#     import pandas as pd
#     url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
#     iris = pd.read_csv(url)
# 
#     return iris


# @app.post("/get-iris")
# def post_iris():
# 
#     import pandas as pd
#     url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
#     iris = pd.read_csv(url)
# 
#     return iris
# 
