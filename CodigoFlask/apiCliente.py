"""
Este documento de python es usado para crear API Cliente.

Autor: William Antonio López Morales
Carne: 200711904
Curso: Software Avanzado
Importación de librerias a utilizar para realización de las API's.
"""
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
notificaciones = []
notificaciones.append({"name": "Frank", "age": 39})


"""
Clase que se encargará de recibir todas las solicitudes que realicen los
clientes para contratar un servicio de viaje en el UBER.
"""


class ClienteSolicitud(Resource):
    """
    Método para recibir las peticiones get del cliente que solicite
    un servicio de transporte UBER.
    """
    def get(self, id):
        respuesta = "Pendiente confirmación, favor de esperar la notificación "
        respuesta += "de confirmación de servicio"
        return {"Solicitud recibida": respuesta}


"""
Clase que se encargará de devolver al cliente todas las nofificaciones así
como respuestas que reciba de parte del servidor por las solicitudes
realizadas.
"""


class ClienteNotifView(Resource):
    """
    Método para devolver las noficaciones a traves del método get hacia el
    cliente.
    """
    def get(self, id):
        return {"Sus Notificaciones son": notificaciones}


"""
Clase que se encargará de recibir del ESB (orquestador) las respuesta
del sistema y se encargará de almacenarla para que el cliente las
pueda visualizar posteriormente en la opcion de ClienteNotifView.
"""


class ClienteNotifSave(Resource):
    """
    Método para devolver las noficaciones a traves del método get hacia el
    cliente.
    """
    def get(self, id):
        notificaciones.append({"name": "Frank", "age": 39})
        return {"Notificacion": "Ha sido almacenada correctamente"}

"""
Direcciones habilitadas para los clientes.
"""
api.add_resource(ClienteSolicitud, '/cliente/solicitar/<id>')
api.add_resource(ClienteNotifView, '/cliente/notifview/<id>')
api.add_resource(ClienteNotifSave, '/cliente/notifsave/<id>')

"""
Comando que levantara el servidor en el puerto 5010.
"""
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5010)
