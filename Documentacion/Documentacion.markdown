#SOFTWARE AVANZADO
##Tarea 2
###Autor: William Antonio López Morales
###Carne: 200711904


**Dirección de GitHub**  
[GitHub](https://github.com/WilliamLopez5/SA_Tarea2_200711904/tree/master "GitHub")

**Lenguaje de programación utilizado:**  
C# con Microsoft Visual Studio 2019

**Servidor:**  
IIS EXPRESS ( proporcionado por Visual Studio 2019 )

**Sistema Operativo**
Windows 10


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
