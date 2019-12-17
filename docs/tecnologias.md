# Tecnologías empleadas y despliegue del proyecto

Los microservicios serán programados en primera instancia en Python, con el uso del framework [Flask](https://www.palletsprojects.com/p/flask/). Se imlementará APIs REST para la comunicación entre microservicios. Las bases de datos serán implementadas con MongoDB. Para el sistema de logs se utilizará [logstash](https://www.elastic.co/products/logstash). La API Gateway será implementada con [ambrassador](https://www.getambassador.io). Y para el sistema de configuración distribuida se usará [etcd](https://etcd.io).

Cada microservicio será archivado y ejecutado en su propio contenedor, y como motor de los contenedores se usará [Docker](https://www.docker.com). Como orquestador de los contenedores y desplegar el proyecto se usará [Kubernete](https://kubernetes.io).
