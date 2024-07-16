import psycopg2

conn = psycopg2.connect(
    database = "fliperama",
    user = "postgres",
    password = "mt260326",
    host = "localhost",
    port = "5432"
)