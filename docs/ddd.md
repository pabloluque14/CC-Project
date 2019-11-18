# Análisis del dominio del problema

 Entidades del dominio del problema:

+ Tienda: Representa un establecimiento físico que oferta productos y/o servicios al consumidor local. Dentro de la aplicación las tiendas contarán con su información básica:
	- Indentificador
	- Nombre.
	- Descripción breve acerca de su negocio.
	- Dirección física.
	- Información de contacto.
	- Valoración de la tienda.
	- Número de transacciones.

+ Producto: Representa un objeto físico o servicio el cuál es ofertado por una tienda en concreto. Los productos ofertados por las tiendas contarán con la siguiente información:
	- Indentificador.
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

También se ha planteado el siguiente objeto de valor:

+ Estadísticas: Las estadísticas son información acerca de la interacción que tienen las personas con las tiendas del sistema. Esta información se generá calculando una puntuación en función de la valoración de la tienda y su número de transacciones. Con esta puntuación se ordenará las tiendas para recomendar las mejores valoradas.
