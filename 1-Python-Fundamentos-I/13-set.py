gamesSet = {"Fifa 23", "Red Dead 2", "Star Wars", "The Legend of Zelda",
            "Mario Odyssey", "Resident Evil 4"}
print(gamesSet)

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 - True e 1 sao considerados o mesmo valor
exampleSet = {"Fifa 23", True , 1 ,90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover um item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)

# Nao possibilita recuperar valores via fatiamenta
