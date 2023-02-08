# Trabajo Práctico Final Foundations
## Molinetes (ejercicio-1)

Este proyecto tiene el objetivo de analizar los viajes realizados en toda la red de subte de la Ciudad Autónoma de Buenos Aires en el año 2021. Para ello se utilizará el siguiente [dataset](https://data.buenosaires.gob.ar/dataset/subte-viajes-molinetes/resource/331515f5-bd2e-4032-b39e-b6318babca95).

Los requerimientos del negocio que se desean saber son los siguientes:
1. Cantidad de viajes por línea en el año, para detectar cuál es la más utilizada.
2. Promedio diario de viajes por línea.
3. De cada línea, cuáles son las estaciones más utilizadas anualmente.
4. Promedio de viajes en cada día de la semana, para ver la variación de viajes entre cada día.
5. Cantidad de viajes por mes, para detectar dónde hay un pico de viajes.

## Solución
En el [docker-compose](https://github.com/itba-cloud-data-engineering/tpf-foundations-2022h2-nmema/blob/main/docker-compose.yml) tenemos 3 servicios:
1. [ejercicio-2](https://github.com/itba-cloud-data-engineering/tpf-foundations-2022h2-nmema/blob/main/docker-compose.yml?plain=1#L3): contenedor con la base de datos Postgres 14.5 donde persisten en un volumen local los datos del dataset.
2. [populate](https://github.com/itba-cloud-data-engineering/tpf-foundations-2022h2-nmema/tree/main/ejercicio-4): contenedor que realiza las operaciones de DDL, descarga e ingesta de datos.
3. [app](https://github.com/itba-cloud-data-engineering/tpf-foundations-2022h2-nmema/tree/main/ejercicio-5): contenedor que realiza las consultas del negocio y luego permite visualizarlas mediante una aplicación de Flask.

Para correr la aplicacion, desde la linea de comando:
```
docker-compose up
```
Luego de la inicializacion de los servicios (tarda aproximadamente entre 1 y 2 minutos) se podrán ver los resultados del reporte en http://localhost:5000/
