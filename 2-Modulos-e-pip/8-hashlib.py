import hashlib

# 1 - Verificar os algoritimos disponiveis
print(hashlib.algorithms_available)

# 2 - Algoritimos disponiveis de acordo com a SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é cria-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 5 - Utilizando md5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())