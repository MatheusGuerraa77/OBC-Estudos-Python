"""
Fatorial de um numero:
1 -> 1
3 -> 3 * 2 * 1 
5 -> 5 * 4 * 3 * 2 * 1
"""

# 1 Fatorial de um numero :
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial (num - 1))
    
number = int(input("Digite o numero para o fatorial :\n"))
print(f"O fatorial de {number} é {factorial(number)}")

# 2 - Soma total de um numero
"""
Fatorial de um numero:
1 -> 1
3 -> 3 + 2 + 1 
5 -> 5 + 4 + 3 + 2 + 1
"""
def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))
    
num = int(input("Digite um numero para a soma : \n"))
print(f"A soma total do {num} é :{total_sum(num)}")