from abc import ABCMeta, abstractmethod
from src.domain.itemResume import ItemResumen

class ItemResumenRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, itemResume:ItemResumen):
        raise NotImplementedError
