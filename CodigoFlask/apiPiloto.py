"""
Este documento de python es usado para crear API Cliente.

Autor: William Antonio López Morales
Carne: 200711904
Curso: Software Avanzado
Importación de librerias a utilizar para realización de las API's.
"""
from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)
notificaciones = []
notificaciones.append({"name": "piloto"})


"""
Clase que se encargará buscar un piloto disponible.
"""


class PilotoSolicitar(Resource):
    """
    Método para solicitar un piloto UBER.
    """
    def get(self, id):
        direccion = 'http://localhost:5000/esb/Rastreo/piloto/solicitar/' + id
        info = requests.get(direccion)
        respuesta = "Se ha enviado solicitud de piloto cercano."
        return {"Solicitud": respuesta}


"""
Clase que se encargará de confirmar los servicios que acepta realizar
el piloto.
"""


class PilotoConfirmar(Resource):
    """
    Método para confirmar las peticiones del cliente que solicite
    un servicio de transporte UBER.
    """
    def get(self, id):
        respuesta = "Se ha confirmado que se prestara el servicio al cliente."
        return {"Solicitud confirmada": respuesta}


"""
Clase que se encargará de devolver al piloto todas las nofificaciones
que reciba de parte del servidor por las solicitudes
realizadas.
"""


class PilotoNotifView(Resource):
    """
    Método para devolver las noficaciones a traves del método get hacia el
    piloto.
    """
    def get(self, id):
        return {"Sus Notificaciones son": notificaciones}


"""
Clase que se encargará de recibir del ESB (orquestador) las respuesta
del sistema y se encargará de almacenarla para que el piloto las
pueda visualizar posteriormente en la opcion de pilotoNotifView.
"""


class PilotoNotifSave(Resource):
    """
    Método para almacenar las noficaciones del piloto.
    """
    def get(self, id, texto):
        notificaciones.append({id: texto})
        return {"Notificacion": "Ha sido almacenada correctamente"}

"""
Direcciones habilitadas para los pilotos.
"""
api.add_resource(PilotoSolicitar, '/piloto/Solicitar/<id>')
api.add_resource(PilotoConfirmar, '/piloto/confirmar/<id>')
api.add_resource(PilotoNotifView, '/piloto/notifview/<id>')
api.add_resource(PilotoNotifSave, '/piloto/notifsave/<id>/<texto>')

"""
Comando que levantara el servidor en el puerto 5020.
"""
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5020)
