from datetime import datetime

from sqlalchemy import null
from src.infraestructure.adapters.db.dbo.itemsProcessFileEntity import ItemProcessFileEntity
from src.domain.itemResume import ItemResumen
from src.application.repository.itemResumeRepository import ItemResumenRepository
from src.infraestructure.adapters.db import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()


class MySQLItemResumenRepository(ItemResumenRepository):
    """Este es la implementacion especifica de MYSQL del repositorio que se definio en la capa de servicio para gestionar todo lo que tenga que ver con las entidades ItemResumen"""
    def __init__(self) -> None:
        super().__init__()
    

    """Descripción de la función
        Parameters
        ----------
        parametro_1 : itemResume
            Es el objeto de dominio que será persistido en la base de datos
        
        Returns
        -------
        mensaje
            return el resultado de ejecutar el servicio
            TODO:realizar un manejo adecuado de las respuesta de los metodos para poder espeficiar codigos de error de negocio
    """
    def save(self, itemResume: ItemResumen):
        dateTimeItemFormat = None
        if(itemResume.itemStartTime!=None and itemResume.itemStartTime!=null):
            dateTimeItemFormat = datetime.strptime(itemResume.itemStartTime,'%Y-%m-%dT%H:%M:%S.000Z')
       
        itemProcessFileEntity = ItemProcessFileEntity(idItem=itemResume.itemId, site=itemResume.itemSite, price=itemResume.itemPrice, startTime=dateTimeItemFormat,
                                                      categoryName=itemResume.categoryName, currencyDescription=itemResume.currencyDescription, sellerName=itemResume.sellerNickName)

        session.add(itemProcessFileEntity)
        session.commit()
        return "created"
