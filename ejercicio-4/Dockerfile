FROM python:3.10.8-buster

# https://wiki.postgresql.org/wiki/Apt
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && curl -sSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && apt-get update \
    && apt-get install -y postgresql-client-common \
        postgresql-client-14 \
    && pip install psycopg2

COPY populate /home/populate

WORKDIR /home/populate

RUN chmod +x init.sh

CMD ["./init.sh"]