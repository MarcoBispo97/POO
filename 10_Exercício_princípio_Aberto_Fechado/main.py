from repositorio import Repositorio
from databases import PostgresDB


db_conn_postgres = PostgresDB()
db_conn_mysql = PostgresDB()
repo = Repositorio()

repo.insert(db_conn_postgres)
repo.select(db_conn_mysql)
