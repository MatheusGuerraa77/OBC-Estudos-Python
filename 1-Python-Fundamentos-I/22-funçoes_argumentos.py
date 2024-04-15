# 1 - Crie uma funçao que receba dois argumentos: o primeiro nome e o segundo nome
def full_name(fname, Lname):
    print(f"Nome completo : {fname} {Lname}")
    
full_name("Rodrigo", "Macedo")

# 2 - Crie uma funçao que some dois numeros via parametros
def sum(a, b):
    return a + b

print(sum(10, 50))

# 3 - Argumentos default numa funçao
def addrees(country="Brasil"):
    print(f"Eu moro no {country}")
    
addrees()
addrees("Canada")

# 4 - Avaliaçao do jogo
def rating_game(qtdRating):
    game_name = input("DIgite o nome do jogo :\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota do jogo :\n"))
        sum += note # sum = sum + note
    print(f"Media de avaliaçao do jogo {game_name} é : {sum / qtdRating}")
rating = int(input("Digite quantas avaliaçoes deseja fazer no jogo :\n"))
rating_game(rating)
rating_game(rating)
rating_game(rating)
