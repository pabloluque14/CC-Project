# Imagen base del contenedor seleccionada
FROM python:3.8-slim-buster

LABEL image = statisticmanager_base_image

# Argumentos del contenedor
ARG PORT2
ARG DB_URI

# Se crean variables de entorono que son asignadas por los argumentos
ENV PORT2=${PORT2}
ENV DB_URI=${DB_URI}

# Directorio base
WORKDIR /

# Copiamos requisitos exclusivos del microservicio
COPY requirements2.txt ./

# Instalar paquetes necesarios
RUN pip3 install --no-cache-dir -r requirements2.txt

# Copiamos los archivos necesarios para levantar el microservicio
COPY src/statistic_manager.py ./
COPY src/datamanager.py ./

# Puerto para conectar con el contenedor
EXPOSE ${PORT2}

# Lanzar el microservicio
CMD gunicorn -b 0.0.0.0:${PORT2} statistic_manager:app