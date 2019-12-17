# CC-Project
[![License: LGPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  [![Build Status](https://travis-ci.com/pabloluque14/CC-Project.svg?branch=master)](https://travis-ci.com/pabloluque14/CC-Project)
[![codecov](https://codecov.io/gh/pabloluque14/CC-Project/branch/master/graph/badge.svg)](https://codecov.io/gh/pabloluque14/CC-Project) [![CircleCI](https://circleci.com/gh/pabloluque14/CC-Project.svg?style=svg)](https://circleci.com/gh/pabloluque14/CC-Project)



Proyecto a desarrollar para la asignatura Cloud Computing del Master de Ingeniería Informática en la UGR.

## ZoneShop

Se va a desarrollar una aplicación denominada ZoneShop, que permitirá a dueños de comercios locales de determinadas localidades ofertar sus servicios o productos a través de un entorno virtual en la nube. Dependiendo del producto o servicio, sete se podrá encragar a través de la aplicación.

## Arquitectura

La arquitectura del sistema estará basada en microservicios. Estos microservicios se han planteado a partir del [Análisis del dominio del problema](docs/ddd.md). Tanto la arquitectura como los microservicios del sistema pueden verse [aquí](docs/arquitectura.md).


## Tecnologías empleadas y despliegue del proyecto
La información respecto a la tecnología del sistema y su despligue en la nube puede encontrarse [aquí](docs/arquitectura.md).

## Dependencias e instalación
Al ser el proyecto construido en Python se deberá disponer de cualquiera de las versiones de este desde la 3.5 hasta la versión 3.8. También se deberá tener instalado las herramientas `pip3` y `Makefile`.

## Herramienta de construcción
buildtool: Makefile

Como herramienta de construcción para este proyecto se ha seleccionado `Makefile`. En primer lugar para instalar todas las dependencias del proyecto se ejecutará el comando:

```
$ make install
```

Para ejecutar los tests sobre lo módulos ya programados y los tests de cobertura, se hará con el siguiente comando:

```
$ make test
```
Los tests se han implementado con el módulo de Python [unittest](https://docs.python.org/3/library/unittest.html). Tiene como ventaja que no necesita instalación adicional y ofrece varias posibilidades para hacer un testeo del código. Para los test de cobertura se ha usado [coverage](https://coverage.readthedocs.io/en/coverage-5.0/#quick-start) el cuál se integra con unittest. Y para los tests de integración continua se ha usado [codecov](https://codecov.io/).

## Integración Continua
En este proyecto se utiliza dos sistemas de integración continua: Travis CI y CircleCI. A continuación se describe que labores hacen cada uno:
+ Travis CI: Travis se encarga de que el proyecto se construye adecuadamente y comprueba que tantos los tests unitarios, de integración y de cobertura se ejecutan sobre los módulos del proyecto correctamente para las versiones del lenguaje que se han especificado en el fichero de configuración y el sistema operativo donde se ha desarrolado el proyecto. Para este proyecto en concreto se comprobará que todo funciona correctamente para las versiones del lenguaje Python desde la 3.5.8 hasta la 3.8.0 en el Sistema Operativo linux. La configuración completa de Travis para este proyecto se encuntra [aquí](.travis.yml).

+ CircleCI: Funciona de forma similar al anterior, solo que este lanza una imagen Docker donde se crea un entorno virtual en el cuál se monta el proyecto. Una vez crealo se "clona" el reposito en el entorno virtual. Para este proyecto la imagen Docker que se usa es de Python 3.7.5. El archivo de configuración completo puede encontrarse [aquí](.circleci/config.yml).


# Licencia
Este proyecto estará bajo licencia [*GNU General Public License v3.0*](https://github.com/pabloluque14/CC-Project/blob/master/LICENSE).
