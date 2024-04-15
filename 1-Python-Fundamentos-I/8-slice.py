gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol 
desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""
# string [inicio:fim] - indice começa na posiçao : 0 / indice final : -1
# 1 - Busque toda string apartir da primeira posiçao
print(gameName[0:])

# 2 - Busque toda string ate a ultima posiçao
print(gameName[:7])

# 3 -Busque toda string da terceira ate a ultima posiçao
print(gameName[2:])

"""
# string [inicio:fim:passo] - indice começa na posiçao : 0 / indice final : -1
passo-determina o incremento.Que por padrao esse numero é o 1.
"""
#4 -Busque toda a string de 2 a 2 caracteres 
print(gameName[::2])

#5 - Busque toda a string nos indices impares
print(gameName[1::2])

# 6 - Inverter uma string de tras pra frente
print(gameName[::-1])