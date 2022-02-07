import csv
from operator import indexOf
from src.domain.itemResume import ItemResumen
from src.utils import constans
from src.infraestructure.adapters.files.itemsFileLoader import ItemsFileLoader


class CSVItemsFileLoader(ItemsFileLoader):
    """Esta es la implementacion especifica para un archivo CSV que hereda de ItemFileLoader"""
    delimiter = None
    encoding = None
    def __init__(self):
        ItemsFileLoader.__init__(self, 'text/csv')
        #default value
        delimiter = ","
        encoding = "utf-8"

    """Sobre escribe el metodo fileRowToObjects que se encarga de la lectura del archivo y convertirlos en objetos de dominio ItemResemen"""
    def fileRowsToObjects(self, file):
        rowsItemResumen = []
        try:
            with open(self.path + constans.PATH_SEPARATOR + self.fileName, 'r', encoding=self.encoding) as file:
                reader = csv.reader(file, delimiter=self.delimiter)
                header = []
                header = next(reader)
                
                for row in reader:
                    itemResumen = ItemResumen(itemSite=row[0], itemId=row[1])
                    rowsItemResumen.append(itemResumen)
            file.close()
            return rowsItemResumen
        except:
            return rowsItemResumen
