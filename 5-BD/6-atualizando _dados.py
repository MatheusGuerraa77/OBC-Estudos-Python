import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor 
'''
Cursor é um interador que permite navegar e manipular os registros em um BD
'''

cursor = connection.cursor()

# 3 - Solicitando dados do usuário
id = int(input("Informe o id do file que deseja atualizar:\n"))
name = input("Informe o novo nome do filme:\n")

# 4 - Atualizando dados
cursor.execute("""
        UPDATE movie set name = ?
        WHERE id = ?
               """, (name, id))
connection.commit()
print("Dados Atualizados com sucesso!")
         
# 5 - Fechando conexão
connection.close()