# CC-Project
[![License: LGPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  [![Build Status](https://travis-ci.com/pabloluque14/CC-Project.svg?branch=master)](https://travis-ci.com/pabloluque14/CC-Project)
[![codecov](https://codecov.io/gh/pabloluque14/CC-Project/branch/master/graph/badge.svg)](https://codecov.io/gh/pabloluque14/CC-Project) [![CircleCI](https://circleci.com/gh/pabloluque14/CC-Project.svg?style=svg)](https://circleci.com/gh/pabloluque14/CC-Project)



Proyecto a desarrollar para la asignatura Cloud Computing del Master de Ingeniería Informática en la UGR.

## ZoneShop

Se va a desarrollar una aplicación denominada ZoneShop, que permitirá a dueños de comercios locales de determinadas localidades ofertar sus servicios o productos a través de un entorno virtual en la nube. Dependiendo del producto o servicio, este se podrá encargar a través de la aplicación.

## Arquitectura

La arquitectura del sistema estará basada en microservicios. Estos microservicios se han planteado a partir del [Análisis del dominio del problema](docs/ddd.md). Tanto la arquitectura como los microservicios del sistema pueden verse [aquí](docs/arquitectura.md).


## Tecnologías empleadas y despliegue del proyecto
La información respecto a la tecnología del sistema y su despliegue en la nube puede encontrarse [aquí](docs/arquitectura.md).

## Dependencias e instalación
Al ser el proyecto construido en Python se deberá disponer de cualquiera de las versiones de este desde la 3.5 hasta la versión 3.8. También se deberá tener instalado las herramientas `pip3` y `Makefile`.

## Herramienta de construcción
buildtool: Makefile

Como herramienta de construcción para este proyecto se ha seleccionado `Makefile`. Esta herramienta permite realizar las siguientes tareas:

  - Instalar las versiones necesarias de los paquetes usados para el proyecto en el entorno donde se vaya a ejecutar. Para ello se usa la herramienta `pip3` para instalar las dependencias que vienen en el fichero `requirements.txt`.

  - Ejecutar los tests unitarios, de integración y de cobertura sobre el proyecto.Los tests se han implementado con el módulo de Python [unittest](https://docs.python.org/3/library/unittest.html). Tiene como ventaja que no necesita instalación adicional y ofrece varias posibilidades para hacer un testeo del código. Para los test de cobertura se ha usado [coverage](https://coverage.readthedocs.io/en/coverage-5.0/#quick-start) el cuál se integra con unittest. Y para los tests de integración continua se ha usado [codecov](https://codecov.io/). Una vez ejecutado los tests se muestra el resultado de la cobertura.

En el [Makefile](Makefile) puede verse que se lleva a cabo cada tarea.
El uso de Makefile es bastante simple, primero para crear un entorno virtual en Python 3 e instalar todas las dependencias del proyecto se ejecutará el comando por terminal:

```
$ make install
```

Para ejecutar los tests sobre lo módulos ya programados y los tests de cobertura, se hará con el siguiente comando:

```
$ make test
```

## Integración Continua
En este proyecto se utiliza dos sistemas de integración continua: Travis CI y CircleCI. A continuación se describe que labores hacen cada uno:
+ Travis CI: Travis se encarga de que el proyecto se construye adecuadamente y comprueba que tantos los tests unitarios, de integración y de cobertura se ejecutan sobre los módulos del proyecto correctamente para las versiones del lenguaje que se han especificado en el fichero de configuración y en el sistema operativo donde se ha desarrollado el proyecto. Para este proyecto en concreto se comprobará que todo funciona correctamente para las versiones del lenguaje Python: 3.5.8, 3.6.9, 3.7.0, 3.7.5 y 3.8.0 (el historial de actualización  de versiones se puede consultar [aquí](https://www.python.org/doc/versions/)). Se ha usado estas versiones debido a su frecuente actualización, todas ellas fueron actualizadas entre 2018 y 2019 por lo que se descarta que puedan quedar obsoletas. Estas versiones se probarán en el sistema operativo Linux y así asegurar que el proyecto es reproducible en diferentes entornos con diferentes versiones del lenguaje de programación usado. La configuración completa de Travis para este proyecto se encuentra [aquí](.travis.yml).

+ CircleCI: Funciona de forma similar al anterior, solo que este lanza una imagen Docker donde se crea un entorno virtual en el cuál se monta el proyecto. Una vez creado se "clona" el repositorio en el entorno virtual. Para este proyecto la imagen Docker que se usa es de Python 3.6.9 (versión de desarrollo). Se ha añadido el uso de cache dentro de la configuración de Circle Ci para que tarde menos en poner marcha en proyecto ya que solo descargará las dependencias obsoletas o que se añadan directamente. La documentación pertinente al "caching" puede encontrarse [aquí](https://circleci.com/docs/2.0/caching/). El archivo de configuración para ver la configuración completa, puede encontrarse [aquí](.circleci/config.yml).


# Licencia
Este proyecto estará bajo licencia [*GNU General Public License v3.0*](https://github.com/pabloluque14/CC-Project/blob/master/LICENSE).
