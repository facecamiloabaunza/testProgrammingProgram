from fileinput import filename
import os
from src.utils import constans
from datetime import datetime

class ItemsFileLoader(object):

    """Esta clase permite abstraer de manera generica algunas funcionalidades para el manejo de la lectura del archivo y da una espeficicacion para el desarrollo de cada uno de los tipos de archivo"""
    contentType = None
    path = None
    fileName = None

    def __init__(self,contentType):
        self.contentType = contentType

    """Descripción de la función
        Parameters
        ----------
        parametro_1 : file
           Contiene el archivo que se procesa en la capa de servicio y que debe ser almacenado de manera temporal para su lectura
        
        Returns
        -------
        mensaje
            Return el archivo almacenado o en su defecto un objeto vacio
            TODO:realizar un manejo adecuado de las respuesta de los metodos para poder espeficiar codigos de error de negocio
    """
    def saveFileToLocalStore(self,file):
        nowTimeStamp = datetime.today()
        timestampStr = nowTimeStamp.strftime("%d%m%Y%H%M%S%f")
        if(len(file.filename.split('.')) > 1):
            self.fileName = constans.SAVE_FILE_NAME_TEMP + timestampStr + \
                constans.FILE_EXTENSION_SEPARATOR+file.filename.split('.')[1]
            self.path = constans.SAVE_FILE_PATH_TEMP
            file.save(os.path.join(self.path, self.fileName))
            return file
        else:
            return None

    """Descripción de la función
        Eliminar el archivo que gestionar el file loader"""
    def deleteItemsFile(self):
        os.remove(self.path+constans.PATH_SEPARATOR+self.fileName)

    def fileRowsToObjects(self,file):
        pass

    def __str__(self):
        return ""
