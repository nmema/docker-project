import psycopg2


print('Creando conexion...')
conn_string = "host='molinetes-db' dbname='postgres' user='postgres' password='postgres'"
conn = psycopg2.connect(conn_string)

cur = conn.cursor()

with open('historico_2021.csv', 'r') as f:
    print('Iniciando carga de datos...')
    cur.execute('TRUNCATE TABLE molinetes')
    cur.execute("SET datestyle TO 'ISO, DMY'") # As in our dataset, the fecha field format is 'DD-MM-YYYY'
    next(f) # Skip the header row.
    cur.copy_from(f, 'molinetes', sep=';')

conn.commit()
print('Carga exitosa!')