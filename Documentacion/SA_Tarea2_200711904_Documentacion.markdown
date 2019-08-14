#SOFTWARE AVANZADO
##Tarea 2
###Autor: William Antonio López Morales
###Carne: 200711904


**Dirección de GitHub**  
[GitHub](https://github.com/WilliamLopez5/SA_Tarea2_200711904/tree/master "GitHub")

**Dirección del Video**  
[YouTube](https://youtu.be/_gdLvQuUsgw "YouTube")

**Lenguaje de programación utilizado:**  
Python 2.7.4       Framework: FLASK



**Sistema Operativo**
Windows 10


**Interacción de los componentes**
El Cliente realiza una peticion Get a través de internet al sistema, el Orquestados ESB recibe la petición y la redirecciona al microservicio de "CLiente". La API cliente solicita al microservicio "Piloto" un piloto. Esta API determina que para poder brindar el servicio de transporte necesita ubicar al piloto con la ubicación mas cercana al cliente, por lo que le solicita a traves dle ESB al API de "Rastreo" que le notifique al piloto mas cercano, luego el sistema de Rastreo le Avisa a los microservicios de Clientes y Pilotos que ya le pueden avisar al piloto que ha sido asignado un viaje y al cliente que ya tiene asignado un piloto, segun corresponda a cada API.

###Diagrama de la solucion MICROSERVICIOS
***
![Diagrama](img/d1.png "Diagrama")

**Orquestador**  
Este componente se encargará de manejar todas las peticiones que se realicen al sistema y determinará que API(Microservicio) será la encargada de atender la peticion que realice y recibira la respuesta y se la volverá a redireccionar a la ubicación correspondiente.

**API Clientes**  
Esta API se encargara de responder todas las solicitudes que hagan los clientes, como crear clientes, loguearse, solicitar vehiculos, y notificara al usuario todas las respuestas que reciba del servidor, como confirmación de que se le brindara el servicio.

**API Pilotos**  
Esta función se encargara de atender peticiones que realicen los pilotos, como crear piloto, notificar pilotos para atender servicio, y recibir respuestas de los pilotos que esten libres y deseen atender servicio.

**API Rastreo**  
Esta API buscara la ubicación de los vehiculos y detectará vehiculos disponibles

**Clientes/Pilotos/Rastreo**  
Son los usuarios finales que interacturán con el sistema

**Base de Datos**  
Es el software que se encarga del almacenamiento y recuperación de la información guardada de los 


