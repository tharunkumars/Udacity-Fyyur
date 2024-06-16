import psycopg2

connection = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")

print("Connection successful!")

connection.close()
