import math

# 1 - Acessar o numero Pi
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessar o numero de Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondando números pra cima e baixo
num1 = 10.4
print(math.ceil(num1))#arredonda pra cima
print(math.floor(num1))#arredonda pra baixo

# 4 - Fatorial de um numero
num2 = int(input("Digite um numero para o fatorial :\n"))
print(math.factorial(num2))

# 5 - Potência de números 
print(math.pow(5,5))

# 6 - Raiz quadrada de um número
print(math.sqrt(169))

# 7 - MDC
mdc = math.gcd(20, 70) # 20 / 70
print(mdc)

# 8 - Logaritmo
print(math.log(10))