gameName = "Fifa23"
gameDescription = """
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online
"""
print(gameName.upper()) # Retornar string em maiusculo
print(gameName.lower()) # Retornar string em minusculo
print(gameName.capitalize()) # Retornar Apenas a primeira letra em maiusculo 
print(gameName.title()) # Retornar Apenas a primeira letra em maiusculo 
print(gameName.center(10 , '-')) # Retorna a string centralizada com caractere de preenchimento
print(gameDescription.find("i")) #Retorna a posiçao de um determinado caractere
print(gameDescription.count("f")) #conta caracteres
print(gameDescription.count("a")) #conta caracteres
print(gameDescription.replace("Fifa", "Pes")) #Altera um elemento por outro
print(gameDescription.split(','))