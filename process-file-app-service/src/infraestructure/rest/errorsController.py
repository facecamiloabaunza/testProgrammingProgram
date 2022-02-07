from flask.views import MethodView


class NotFoundResourceError(MethodView):
    """Esta clase es la clase controladora el acceso a recursos que no han sido definidos en el catalogo de rutas"""
    def get(self,error):
        return f"API resource not found, detail: {error}"

