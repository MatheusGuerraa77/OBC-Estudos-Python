gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted", 90.50]

# 1 - Interando valores de uma lista
for game in gamesList:
    print(game)
   
# 2 - Quando a condiçao for atendida , o loop sera encerrado
for game in gamesList:
    if game == "Red Dead 2":
        break 
    print(game)
    
# 3 - Quando a condiçao for atendida ,o loop vai para a proxima interaçao
for game in gamesList:
    if game == "Red Dead 2":
        continue
    print(game)
    
# 4 - Avaliaçao do jogo
gameName = input("Digite o nome do jogo:\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo:\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo:\n"))
    sum += note # sum = sum + note
print(f"A media de avaliaçao do jogo {gameName} é : {sum/gameRating :.2f}")
