import psycopg2

connection1 = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")

cursor = connection1.cursor()

## drop any existing todos table
cursor.execute("DROP TABLE IF EXISTS TODO_TABLE;")

## (note: triple quotes allow multiline text in python)
cursor.execute("""
  CREATE TABLE TODO_TABLE (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")

cursor.execute('INSERT INTO TODO_TABLE (id, description) VALUES (%s, %s);', (1, "Method1"))

cursor.execute('INSERT INTO TODO_TABLE (id, description) VALUES ( %(id)s, %(description)s );', 
               {
                'id': 2,
                'description': "Method2"
               }
               )

## Executing using String Statement and tupple  
SQL = 'INSERT INTO TODO_TABLE (id, description) VALUES (%(id)s, %(description)s);'
data = {
  'id': 3,
  'description': "Method3"
}
cursor.execute(SQL,data)
    
## commit, so it does the executions on the db and persists in the db
connection1.commit()

## cursor.fetchall()
## cursor.fetchmany(3)
## cursor.fetchone()
cursor.execute("SELECT * from TODO_TABLE")
print("fecthall")
print(cursor.fetchall())
print("\n\n")
      
cursor.execute("SELECT * from TODO_TABLE")
print("fecthmany")
print(cursor.fetchmany(2))
print("\n\n")

cursor.execute("SELECT * from TODO_TABLE")
print("fecthOne")
print(cursor.fetchone())
print("\n\n")

cursor.close()
connection1.close()
