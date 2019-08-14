SOFTWARE AVANZADO
Tarea 2
Autor: William Antonio López Morales
Carne: 200711904

Tarea 2. Crear un ESB orquestador de microservicios para: Clientes, Pilotos y Rastreo de Vehículos

Dirección de GitHub
[GitHub](https://github.com/WilliamLopez5/SA_Tarea2_200711904/tree/master "GitHub")

Dirección del Video:
[YouTube](https://youtu.be/_gdLvQuUsgw "YouTube")

Lenguaje de programación utilizado:  
Python 2.7.4       Framework: FLASK

Sistema Operativo:
Windows 10


Standard de Codificación utilizado:
plugin de Visual Code "Linting Python: Pep8 (pycodestyle)"

Se cuenta con 4 Archivos API escritos en el lenguaje python con el microFramework FLASK:
apiESB.py  
cumple con las funciones de orquestador, redireccionando cada peticion al correspondiente
Microservicio.

apiCliente.py
Atiende todas las peticiones relacionadas con los clientes

apiPiloto.py
Atiende las peticiones relacionadas con los pilotos

apiRasteo.py
Determina las ubicaciones de los clientes y pilotos

