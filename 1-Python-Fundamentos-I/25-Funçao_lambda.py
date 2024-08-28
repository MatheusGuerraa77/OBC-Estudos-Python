# 1 -Funçao de potencia de numero
power = lambda num: num ** 2

# 2 -Funçao que verifica se o numero é par
pair = lambda x: x % 2 == 0

# 3 - Funçao que divide um numero por outro
divNum = lambda x,y: x / y

# 4 - Funçao que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10, 2))
print(divNum(6, 2))
print(reverse("Python"))
print(reverse("Javascript"))