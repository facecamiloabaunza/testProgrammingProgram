from src.domain.itemResume import ItemResumen
from src.infraestructure.adapters.files.itemsFileLoader import ItemsFileLoader
from src.utils import constans


class TXTItemsFileLoader(ItemsFileLoader):


    delimiter = None
    encoding = None

    def __init__(self):
        ItemsFileLoader.__init__(self, 'text/plain')


    def fileRowsToObjects(self,file):
        rowsItemResumen = []
        try:   
            with open(self.path + constans.PATH_SEPARATOR + self.fileName, 'r', encoding=self.encoding) as f:
                lines = f.readlines()
                for line in lines:
                    data =line.strip().split(self.delimiter)
                    if(len(data)>=2):
                        itemResumen = ItemResumen(itemSite=data[0], itemId=data[1])
                        rowsItemResumen.append(itemResumen)
            return rowsItemResumen
        except:
            return rowsItemResumen
