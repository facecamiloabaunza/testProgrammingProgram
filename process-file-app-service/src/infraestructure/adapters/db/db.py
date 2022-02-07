from src.config import DevelomentConfig
from flask import session, current_app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#TODO: Revisar la variable
engine = create_engine(DevelomentConfig.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
