from sqlalchemy import Column, Integer, String
from src.domain.parameter import Parameter
from src.infraestructure.adapters.db.db import Base

class ParameterEntity(Base):
    """Mapea a nivel del servicio la tabla parametros la cual contiene la tuplas llave valor importantes para el funcionamiento y configuracion de la logica de negocio"""
    __tablename__ = 'parameters'
    id = Column(
        Integer,
        primary_key=True
    )
    code = Column(
        String(45),
        nullable=False
    )
    value = Column(
        String(200),
        nullable=False
    )
    description = Column(
        String(400),
        nullable=False
    )

    def mapperToDomain(self):
        return Parameter(self.id,self.code,self.value)


