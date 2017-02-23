import psycopg2 as pg
import pandas.io.sql as psql

# get connected to the database, dont forget to change the password
connection = pg.connect("dbname=aligulac user=postgres password=*YOUR-DATABASE-PASSWORD*")

dataframe = psql.read_sql_query('SELECT * FROM "match"', connection)
