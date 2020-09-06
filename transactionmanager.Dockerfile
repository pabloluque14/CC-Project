# Imagen base del contenedor seleccionada
FROM python:3.8-slim-buster

LABEL image = transactionmanager_base_image

# Argumentos del contenedor
ARG PORT3
ARG DB_URI

# Se crean variables de entorono que son asignadas por los argumentos
ENV PORT3=${PORT3}
ENV DB_URI=${DB_URI}

# Directorio base
WORKDIR /

# Copiamos requisitos exclusivos del microservicio
COPY requirements2.txt ./

# Instalar paquetes necesarios
RUN pip3 install --no-cache-dir -r requirements2.txt

# Copiamos los archivos necesarios para levantar el microservicio
COPY src/transaction_manager.py ./
COPY src/datamanager.py ./

# Puerto para conectar con el contenedor
EXPOSE ${PORT3}

# Lanzar el microservicio
CMD gunicorn -b 0.0.0.0:${PORT3} transaction_manager:app