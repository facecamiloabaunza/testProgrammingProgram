from sqlalchemy import Column, DateTime, Float, Integer, String
from src.infraestructure.adapters.db.db import Base

class ItemProcessFileEntity(Base):
    """Mapea a nivel del servicio la tabla itemsProcessFile que va alojar todos los servicios que se procesan"""

    __tablename__ = 'itemsProcessFile'
    id = Column('id', Integer, primary_key=True)
    idItem = Column('idItem',  String(100))
    site = Column('site', String(100), nullable=False)
    price = Column('price', Float, nullable=True)
    startTime = Column('startTime', DateTime, nullable=True)
    categoryName = Column('categoryName', String(200), nullable=True)
    currencyDescription = Column('currencyDescription', String(200), nullable=True)
    sellerName = Column('sellerName', String(350), nullable=True)
