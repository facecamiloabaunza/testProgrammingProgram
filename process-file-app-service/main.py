
from src.app import app
from src.config import config
"""Inicializa todo el servicio indicando cuales variables del ambiente se quiere cargar"""
if(__name__ =='__main__'):
    app.config.from_object(config['development'])
    app.run()