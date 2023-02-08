#!/bin/bash

echo "Creando tabla molinetes sino existe..."
psql "postgres://postgres:postgres@molinetes-db:5432/postgres" -f ejercicio-3.sql

echo "Obteniendo dataset para popular..."
curl -o historico.zip https://cdn.buenosaires.gob.ar/datosabiertos/datasets/sbase/subte-viajes-molinetes/molinetes-2021.zip
unzip historico.zip
python -u populate.py
rm historico.zip historico_2021.csv