
from src.infraestructure.rest.controller import *
from src.infraestructure.rest.errorsController import NotFoundResourceError

"""routes.py permite controlar cada una de las rutas de manera centralizada que el el servicio contiene"""
routes = {
    "ItemsProcessFileRoute":"/items/processFile","items_process_file_controller":ItemsProcessFileController.as_view("process_file"),
    "PingRoute":"/ping","ping_controller":ItemsProcessFileController.as_view("ping"),
    "notFoundRoute":404, "not_found_controller": NotFoundResourceError.as_view("not_found")
}