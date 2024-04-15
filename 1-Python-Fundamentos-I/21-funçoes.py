# 1 - Funçao para imprimir Hello Wolrd
def wellcome():
    print("Hello World")
    
wellcome()

# 2 -Funçao para somar dois numeros
def sum():
    #print(5 + 4)
    return 5 + 4
    
print(sum())

# 3 -Funçao para cadastrar um jogo
def create_game():
    name= input("Digite o nome do jogo:\n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo:\n")) 
    gamePrice = float(input("Digite o preço do jogo:\n"))
    noteRating = float(input("Digite a nota de avaliaçao do jogo :\n"))
    
    print(f"{name} - R$ {gamePrice}")
    
create_game()
create_game()

