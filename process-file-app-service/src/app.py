from flask import Flask
from src.infraestructure.rest.routes.routes import *

"""App inicializa la aplicacion flask y levante el servidor del servicio"""
app = Flask(__name__)
app.add_url_rule(routes['ItemsProcessFileRoute'],view_func=routes['items_process_file_controller'])
app.add_url_rule(routes['PingRoute'],view_func=routes['ping_controller'])
app.register_error_handler(routes['notFoundRoute'],routes['not_found_controller'])





