import pandas as pd
from sqlalchemy import create_engine
from queries import questions


conn = 'postgresql+psycopg2://postgres:postgres@molinetes-db:5432/postgres'
engine = create_engine(conn)

with open('./templates/index.html', 'w') as file:
    for _, question in questions.items():
        df = pd.read_sql(question['query'], con=engine)
        file.write('<center><p>' + question['label'] + '</p></center>' + '\n')
        file.write('<center>' + df.to_html(index=False) + '</center>' + '\n')
