
# Arquitectura

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
La información del sistema se guardará en dos bases de datos separadas. Una albergará la información de a las tiendas y sus productos y la otra albergará la información de las transacciones.
