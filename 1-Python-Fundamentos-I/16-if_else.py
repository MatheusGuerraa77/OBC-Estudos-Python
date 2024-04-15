name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Informe o ano de lançamento do jogo\n"))
classification = float(input("Informe a nota de classificação do jogo\n"))

if classification > 8.0 and yearLaunch > 2015:
    print(f"O jogo {name} é bom. Recomendo jogá-lo.")
else:
    print(f"O jogo {name} ainda nao atingiu uma boa nota.Por isso nao recomendo.")
    