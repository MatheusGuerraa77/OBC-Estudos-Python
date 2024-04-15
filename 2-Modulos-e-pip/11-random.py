import random

# 1 - Selecionar valor aleatorio de uma lista
list1 = [7, 6, 4, 3, 2, 1]
print(random.choice(list1))

# 2 - Gera um numero aleatorio em um intervalo de valores 
r1 = random.randint(5, 15)
print(r1)

# 3 - Seleciona caractere aleatorio de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatorio
# Sintaxe : random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))
s = "Ola mundo"
print(random.sample(s, 2))
