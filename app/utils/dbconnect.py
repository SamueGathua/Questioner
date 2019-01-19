import os
import psycopg2
from tables import Tables
URL = "dbname=questionerdb host=localhost port=5432 user=postgres password='root'"
DB_URL = os.getenv('DATABASE_URL')

def init_db():
    con = psycopg2.connect(URL)
    return con

def create_tables():

    connect = init_db()
    cursor = connect.cursor()
    tb = Tables()
    queries = tb.table_queries()
    for action in queries:
        cursor.execute(action)
        connect.commit()
    cursor.close()
