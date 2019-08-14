"""
Este documento de python es usado para crear API ESB.

Este sistema se encargara de recibir las peticiones que realice el cliente
y las redireccionara al microservicio encargado de atender y resolver
cada peticion

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
notificaciones.append({"name": "Frank", "age": 39})


"""
Clase que se encargará redireccionar a la api cliente
las solicitudes recibidas.
"""


class ESBClienteSolicitud(Resource):
    """
    Método para recibir las peticiones get del cliente que solicite
    un servicio de transporte UBER.
    """
    def get(self, id):
        direccion = 'http://localhost:5010/cliente/solicitar/' + id
        info = requests.get(direccion)
        return {"Solicitud recibida": info.text}


"""
Clase que se encargará de guardar las notificaciones al cliente.
"""


class ESBClienteNotifSave(Resource):
    """
    Método para recibir las peticiones get del cliente que solicite
    un servicio de transporte UBER.
    """
    def get(self, id, texto):
        direccion = 'http://localhost:5010/cliente/notifsave/'
        direccion += id + '/' + texto
        info = requests.get(direccion)
        return {"Solicitud recibida": info.text}


"""
Clase que se encargará de enviar las notificaciones al cliente.
"""


"""
Clase que se encargará de recibir todas las solicitudes que realicen los
clientes para contratar un servicio de viaje en el UBER.
"""


class ESBClienteNotifView(Resource):
    """
    Método para recibir las peticiones get del cliente que solicite
    un servicio de transporte UBER.
    """
    def get(self, id):
        direccion = 'http://localhost:5010/cliente/notifview/' + id
        info = requests.get(direccion)
        return {"Solicitud recibida": info.text}


class ESBPilotoNotifSave(Resource):
    """
    Método para recibir las peticiones get del cliente que solicite
    un servicio de transporte UBER.
    """
    def get(self, id, texto):
        direccion = 'http://localhost:5020/piloto/notifsave/'
        direccion += + id + '/' + texto
        info = requests.get(direccion)
        return {"Solicitud recibida": info.text}


"""
Clase que se encargará de recibir todas las solicitudes que realicen los
pilotos para contratar un servicio de viaje en el UBER.
"""


class ESBPilotoNotifView(Resource):
    """
    Método para recibir las peticiones get del cliente que solicite
    un servicio de transporte UBER.
    """
    def get(self, id):
        direccion = 'http://localhost:5020/piloto/notifview/' + id
        info = requests.get(direccion)
        return {"Solicitud recibida": info.text}



"""
Clase que se encargará de solicitar un piloto disponible y lo asignara a un
cliente.
"""


class ESBSolicitarPiloto(Resource):
    """
    Método para solicitar un piloto para asignar a un cliente.
    """
    def get(self, id):
        direccion = 'http://localhost:5020/piloto/notifsave/'
        direccion += id + '/' + 'Viaje_Asignado'
        info = requests.get(direccion)
        direccion = 'http://localhost:5010/cliente/notifsave/'
        direccion += id + '/' + 'Viaje_Asignado'
        info = requests.get(direccion)
        return {"Sus Notificaciones son": "Se ha solicitado piloto"}


"""
Clase que se encargará de solicitar un piloto disponible y lo asignara a un
cliente.
"""


class ESBRastreoSolicitarPiloto(Resource):
    """
    Método para solicitar que rastreo ubique un piloto
    cercano y disponible para asignar a un clinete.
    """
    def get(self, id):
        direccion = 'http://localhost:5030/rastreo/get/piloto/' + id
        info = requests.get(direccion)
        return {"Sus Notificaciones son": "Se ha hecho la solicitud a un piloto cercano"}


"""
Direcciones habilitadas para los clientes.
"""
api.add_resource(ESBClienteSolicitud, '/esb/cliente/solicitar/<id>')
api.add_resource(ESBClienteNotifView, '/esb/cliente/notifview/<id>')
api.add_resource(ESBClienteNotifSave, '/esb/cliente/notifsave/<id>/<texto>')
api.add_resource(ESBSolicitarPiloto, '/esb/piloto/solicitar/<id>')
api.add_resource(ESBRastreoSolicitarPiloto, '/esb/rastreo/piloto/solicitar/<id>')
api.add_resource(ESBPilotoNotifSave, '/esb/cliente/notifsave/<id>/<texto>')
api.add_resource(ESBPilotoNotifView, '/esb/piloto/notifview/<id>')


"""
Comando que levantara el servidor en el puerto 5000.
"""
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
