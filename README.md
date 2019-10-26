# CC-Project
Proyecto a desarrollar para la asignatura Cloud Computing del Master de Ingenieria Informática en la UGR

# Descripción del problema

Actualmente es bastante notirio el auge que está teniendo las grandes superficies comerciales ya sean las grandes marketplaces online como Amazon o Zalando o los mismo centros comerciales situados a las afueras de las ciudades, los cuales son cada vez más grandes y atraen a gran número de consumidores. Por el contrario el gran perjudicado en esta expansión está siendo el comercio local, el cúal está en declive y se ve cada vez con menos frecuencia en los barrios debido al poco atractivo que este muestra hacia el consumidor o su distribución en la localidad, al no encontrarse todos estos vendedores locales en un mismo emplazamiento como puede ser un centro comercial 

# Solución al problema

Para solucionar esto y fomentar el comercio de las tiendas locales se propone la creación de un servicio online que permita darse de alta tanto a comercios locales como a consumidores. En este servicio los comercios locales pondrán en conocimiento del consumidor los productos e incluso servicios que ofrecen (en el caso de zapaterías puede ser arreglo de zapatos por X euros). El consumidor tendrá una vista conjunta de todos los productos y servicios de las tiendas de su localidad en el cuál si le interesa alguno de los ofertados pueda acceder a la información de la tienda y su localización si quiere ir a ella.

# Arquitectura 

La arquitectura del sistema estará basada en microservicios. Estos microservicios serán los siguientes: microservicio de gestión de usuarios, microservicios de gestión de tiendas y microservicio de gestión de estadísticas. La siguiente imagen muestra la estructura que tendrá en un principio la arquitectura del sistema.
![](docs/imagenes/arquitecturaSistema.png)

## Microservicio de gestión de usuarios
Este microservicio realizará las tareas de agregar nuevos usuarios, eliminar usuarios, modificar sus datos y permitir iniciar sesión en el sistema. A través de él los usuarios podrán ver el listado de tiendas, ver sus productos y servicios y dejar reseñas de como ha sido su experiencia con la tienda.

## Microservicio de gestión de tiendas
Este microservicio realizará las tareas de agregar nuevas tiendas, eliminar tiendas, modificar sus datos y permitirá iniciar sesión el sistema. A  través de él las tiendas pondrá subir sus productos y servicios que ofrezcan, y dar a conocer su ubicación y nombre.

## Microservicio de gestión de estadísticas
Este microservicio realizará las tarea de controlar el registro de tiendas mejor valoradas en base a la experiencia de los usuarios. Para así posicionar por encima en el listado a las tiendas mejor valoradas.

##Microservicio de LOG
Este microservicio realizará la tarea de conectar los microservicios anteriores.

# Bases de datos

A continuación se va a explicar las dos bases de datos planteadas para este proyecto.

## Base de datos de Usuarios
Esta base de datos albergará la infromación relacionada con los usuarios del sistema.

## Base de datos de Tiendas
Esta base de datos albergará la información relacionada con las tiendas del sistema.




