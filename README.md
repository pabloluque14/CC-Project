# CC-Project
Proyecto a desarrollar para la asignatura Cloud Computing del Master de Ingeniería Informática en la UGR.

# ZoneShop

Se va a desarrollar una aplicación denominada ZoneShop, que permitirá a dueños de comercios locales de determinadas localidades ofertar sus servicios o productos a través de un entorno virtual en la nube. Dependiendo del producto o servicio, sete se podrá encragar a través de la aplicación.

# Análisis del dominio del problema

Dentro del dominio del problema se encuentran las siguientes entidades:

+ Tienda: Representa un establecimiento físico que oferta productos y/o servicios al consumidor local. Dentro de la aplicación las tiendas contarán con su información básica:
	- Nombre.
	- Descripción breve acerca de su negocio.
	- Dirección física.
	- Información de contacto.
	- Valoración de la tienda.
	- Número de transacciones.

+ Producto: Representa un objeto físico o servicio el cuál es ofertado por una tienda en concreto. Los productos ofertados por las tiendas contarán con la siguiente información:
	- Nombre.
	- Descripción breve.
	- Precio.
	- Indicador de que el producto o servicio se puede adquirir online a través de la plataforma, de lo contrario solo se ofertará de manera física en la tienda.

+ Transacción: Una transacción es un intercambio (o pago) que se realiza entre dos entidades o sujetos. En el sistema se realizarán pagos de las personas que accedan a la aplicación, a las tiendas por los productos o servicios que estas ofrecen. Dentro de la aplicación las transacciones contarán con la siguiente información:
	- Indentificador de la transacción.
	- Nombre del  comprador.
	- Nombre de la tienda.
	- Servicio o producto de la tienda vendedora.
	- Precio pagado por el comprador.
+ Estadísticas: Las estadísticas son información acerca de la interacción que tienen las personas con las tiendas del sistema. Esta información se generá calculando una puntuación en función de la valoración de la tienda y su número de transacciones.

# Arquitectura

La arquitectura del sistema estará basada en microservicios. Estos microservicios serán los siguientes:

+ Shop-Manager: La labor principal de este microservicio será administrar las tiendas de la aplicación. Para ello implementará las siguientes funcionalidades:
	- Creación de tiendas.
	- Modificación de los datos de las tiendas.
	- Eliminación de las tiendas.
	- Añadir productos de las tiendas.
	- Eliminar productos de las tiendas.
	- Modificar los productos de las tiendas.

+ Transactions-Manager: La labor de este microservicio será el de procesar el pago por los productos que se oferten de manera online de las tiendas. También se encargará de generar el resguardo de la compra y registrarla.

+ Statistics-Manager: La labor de este microservico será la de recoger las estadísticas de ventas y reseñas de las tiendas para asignarles una puntuación en base a ellas y así ordenarlas según las de mayor puntuación.


La siguiente imagen muestra la estructura que tendrá en un principio la arquitectura del sistema.
![](docs/imagenes/arquitecturaSistema.png)

# Servicios
Los servicios que se emplearán para este proyecto serán los siguientes:

+ Sistema de Logs.

+ API Gateway.

+ Sistema de configuración distribuida.


# Bases de datos

A continuación, se va a explicar las dos bases de datos planteadas para este proyecto.

## Tiendas
En esta base de datos se almacenará la información relacionada con las tiendas del sistema.

## Transacciones
En esta base de datos se almacenará la información relacionada con las transacciones del sistema.

# Tecnologías empleadas
Los microservicios serán programados en primera instancia en Python, con el uso del framework Flask. Se imlementará APIs REST para la comunicación entre microservicios. Y para las bases de datos se usará MongoDB.

# Licencia
Este proyecto estará bajo licencia [*GNU General Public License v3.0*](https://github.com/pabloluque14/CC-Project/blob/master/LICENSE).
