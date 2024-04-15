# 1 -Conta letras maiusculas e minusculas
def check_char(text):
    type ={"Upercase": 0, "Lowercase":0}
    for char in text:
        if char.isupper():
            type["Upercase"] += 1
        elif char.islower():
            type["Lowercase"] += 1
    print("Texto original:", text)
    print("Numero de letras Maiusculas:", type["Upercase"])
    print("Numero de letras Minusculas:", type["Lowercase"])
check_char("A Melhor Forma De Prever o Futuro é Cria-lo")

# 2 -Verifica numero par ou impar
def verify_num(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd
print(verify_num([1, 2, 4, 6, 5, 7, 11, 20, 13]))
