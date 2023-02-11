FROM python:3.10.8-buster

RUN pip install pandas sqlalchemy==1.4 psycopg2 flask

COPY app /home/app

WORKDIR /home/app

EXPOSE 5000

RUN chmod +x init.sh

CMD ["./init.sh"]