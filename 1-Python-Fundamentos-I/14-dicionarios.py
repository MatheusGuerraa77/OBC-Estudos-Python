gameFifa = {
    "price": 90.55,
    "yearLaunch": 2022,
    "version": 2023,
    "classification": 8.5,
    "genre" : ["esporte","familia"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 -Recuperar um elemento do dicionario
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscar apenas as chaves do dicionario
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionario
print(gameFifa.values())

#4 - Buscar itens do dicionario com chave e valor
print(gameFifa.items())

#5 - Adicionar itens no dicionario
gameFifa["players"] = 2
print(gameFifa)

# 6 - atualizar itens no dicionariogam
gameFifa.update({"players": 1})
print(gameFifa)


# 7 - Remover itens no dicionario 
gameFifa.pop("players")
print(gameFifa)
