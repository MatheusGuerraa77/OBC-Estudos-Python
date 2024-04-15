teams = {}
done = False

# Funçao para listar times
def print_teams():
    print("Times listados")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")
# funçao para listar jogadores de um time 
def print_team_players(team):
    print(f"jogadores do{team['name']}")       
    for i, player in enumerate (team['players']):
        print(f"{i+1}. {player}")
        
while not done:
    #Opçoes no programa 
    print("O que voce deseja fazer ?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogadore em um time")
    print("5. Remover jogador de um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input(">")
    if choice == "1":
        team_name = input("Digite o nome do time:\n")
        teams[team_name] = {'name' : team_name, 'players':[]}
        print("time adicionado")
    elif choice == "2":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja remover:\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print("Time removido")
        else:
            print("Numero do time invalido")
    elif choice == "3":
        print_teams()
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja adicionar o jogador :\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Informe o nome do jogador :\n")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time")
        else:
            print("Numero do time esta invalido!")
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja remover o jogador :\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o numero do jogador que deseja remover :\n"))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num -1]
                print("Jogador removido do time!")
            else:
                print("Numero do jogador invalido!")
        else:
            print("Numero do time invalido!")
    elif choice == "6":
        print_teams()
        team_num = int(input("Informe o numero do time que deseja listar os jogadores :\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
        else:
            print("Numero do time invalido!")
            
    elif choice == "7":
        done = True
    else:
        print("Opçao inválida")