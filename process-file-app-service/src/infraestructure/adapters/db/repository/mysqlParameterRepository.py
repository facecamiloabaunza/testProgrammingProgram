from operator import and_
from src.domain.parameter import Parameter
from src.domain.itemResume import ItemResumen
from src.infraestructure.adapters.db import db
from src.application.repository.parameterRepository import ParameterRepository
from src.infraestructure.adapters.db.dbo.parameterEntity import ParameterEntity
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()


class MySQLParameterRepository(ParameterRepository):
    """Este es la implementacion especifica de MYSQL del repositorio que se definio en la capa de servicio para gestionar todo lo que tenga que ver con las entidades de parametros del servicio"""
    def __init__(self) -> None:
        super().__init__()

    """Descripción de la función    
        Parameters
        ----------
        parametro_1 : codeParam
            el codigo del parametro con el que se realizará la consulta a la base de datos
        parametro_1 : value
            el valor del parametro con el que se realizará la consulta a la base de datos
        
        los dos parametros actuan como una validacion Y para la logica de la consulta
        Returns
        -------
       parameterDomain
            return una entidad de domonio con la cual se tiene acceso a la informacion del parametros
            TODO:realizar un manejo adecuado de las respuesta de los metodos para poder espeficiar codigos de error de negocio
    """
    def queryByCodeValue(self, codeParam,value):
        session = Session()
        parameters = session.query(ParameterEntity).filter(
            and_(ParameterEntity.code ==codeParam,ParameterEntity.value == value)
        )
        parametersDomain =list(map(lambda param:param.mapperToDomain(),parameters))
        return parametersDomain
    
    """Descripción de la función
        Parameters
        ----------
        parametro_1 : codeParam
            Codigo con el que se buscara el parametro que contiene este valor en el codigo
        
        Returns
        -------
        mensaje
            return una entidad de domonio con la cual se tiene acceso a la informacion del parametros
            TODO:realizar un manejo adecuado de las respuesta de los metodos para poder espeficiar codigos de error de negocio
    """
    def queryByCode(self, codeParam):
        session = Session()
        parameters = session.query(ParameterEntity).filter(
            ParameterEntity.code ==codeParam
        )
    
        parametersDomain =list(map(lambda param:param.mapperToDomain(),parameters))
        return parametersDomain