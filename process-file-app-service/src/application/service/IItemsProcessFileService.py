from abc import abstractclassmethod, abstractmethod
from abc import ABCMeta

class IItemsProcessFileService(metaclass=ABCMeta):
    @abstractmethod
    def processItemsFile(self,file,contentType):
        pass
    