from abc import ABCMeta, abstractmethod
from src.domain.parameter import Parameter

class ParameterRepository(metaclass=ABCMeta):
    @abstractmethod
    def queryByCodeValue(self, codeParam,value):
        raise NotImplementedError

    def queryByCode(self, codeParam):
        raise NotImplementedError


