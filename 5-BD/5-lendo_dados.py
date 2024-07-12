import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor 
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 - Lendo dados de uma tabela

data = cursor.execute("""
        SELECT * FROM movie 
                      """)
print(data.fetchall())

# 4 - Interando os dados
for row in cursor.execute("SELECT * FROM movie"):
    print(f"{row}\n")

# 5 - ordenando os dados pelo Score
for row in cursor.execute("SELECT * FROM movie ORDER BY score desc"):
    print(f"{row}")

# 6 - Fechando conexão
connection.close()