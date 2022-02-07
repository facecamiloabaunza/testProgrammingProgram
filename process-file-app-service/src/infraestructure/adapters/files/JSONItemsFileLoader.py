from src.infraestructure.adapters.files.itemsFileLoader import ItemsFileLoader
from src.utils import constans

class JSONItemsFileLoader(ItemsFileLoader):
    """Esta es la implementacion especifica para un archivo JSON que hereda de ItemFileLoader"""
    encoding = None

    def __init__(self):
        ItemsFileLoader.__init__(self, 'application/json')
    
    """Sobre escribe el metodo fileRowToObjects que se encarga de la lectura del archivo y convertirlos en objetos de dominio ItemResemen"""
    def fileRowsToObjects(self,file):
        print("entro al codigo")
        rowsItemResumen = []
        try:
              with open(self.path + constans.PATH_SEPARATOR + self.fileName, 'r', encoding=self.encoding) as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
                    #TODO: ESTE METODO SE DEBE IMPLEMENTAR CON LA LOGICA DE UN JSONLINES
                return rowsItemResumen
        except:
            return rowsItemResumen
