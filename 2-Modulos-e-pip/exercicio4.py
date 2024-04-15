import random

done = False
while not done:
    print("O que voce deseja fazer?")
    print("1.Adivinhar um numero")
    print("2.Sair")
    
    choice = input(">")
    if choice == "1":
        print("=====Advinhe um numero de 1 a 10======\n")
        number = int(input("Digite um numero de 1 a 10 :\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabens. Voce Acertou!")
        else:
            print(f"Tente novamente. O numero sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opçao Invalida. Escolha uma opçao entre 1 e 2")