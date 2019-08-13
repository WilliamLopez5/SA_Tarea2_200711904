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


"""
Clase que se encargará del manejo de las posiciones de clientes.
"""


class RastreoPosCliente(Resource):
    """
    Método para devolver el valor de la posicion de los clientes
    latitud y logitud.
    """
    def get(self, id):
        respuesta = "Se ha confirmado que se prestara el servicio al cliente."
        return {"Solicitud confirmada": respuesta}


"""
Clase que se encargará de devolver la posicion de los pilotos.
"""


class RastreoPosPiloto(Resource):
    """
    Método para devolver el valor de la posicion de los pilotos
    latitud y logitud.
    """
    def get(self, id):
        return {"Sus Notificaciones son": notificaciones}


"""
Clase que se encargará de determinar al mejor piloto para brindar
el servicio dependiendo de su posición
"""


class RastreoGetPiloto(Resource):
    """
    Método para determinar cual es el piloto mas optimo a brindar el servicio.
    """
    def get(self, id):
        return {"piloto": "25"}

"""
Direcciones habilitadas para solicitar Rastreo.
"""
api.add_resource(RastreoPosCliente, '/rastreo/posicion/cliente/<id>')
api.add_resource(RastreoPosPiloto, '/rastreo/posicion/piloto/<id>')
api.add_resource(RastreoGetPiloto, '/rastreo/posicion/piloto/<id>')

"""
Comando que levantara el servidor en el puerto 5030.
"""
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5030)
