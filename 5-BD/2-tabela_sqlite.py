import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor 
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Criando a tabela
cursor.execute("""
   CREATE TABLE movie(
       id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       year INTEGER NOT NULL,
       score REAL NOT NULL
   );         
               """)

# 4 - fechando a conexão
print("Tabela criada com sucesso!")
connection.close()
