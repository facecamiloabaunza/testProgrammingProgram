import json
from flask import request
from flask.views import MethodView
from src.application.service.ItemsProcessFileServiceImp import ItemsProcessFileServiceImp
import urllib.request

itemsProcessFile = ItemsProcessFileServiceImp()



class ItemsProcessFileController(MethodView):
    """Esta clase es la clase controladora de la capa REST del servicio web"""


    """Descripción de la función
        Parameters
        ----------
        parametro_1 : fileInput
            Indica el archivo que es enviado por el cliente del servicio y que sera posteriormente ejecutado
        
        Returns
        -------
        mensaje
            return el resultado de ejecutar el servicio
            TODO:realizar un manejo adecuado de las respuesta de los metodos para poder espeficiar codigos de error de negocio
    """
    def post(self):
        file = request.files['fileInput']
        return itemsProcessFile.processItemsFile(file, file.content_type)

    def get(self):
        return "OK"
        