
# 1 - Calculo da distancia
distance = float(input("Digite a distancia a percorrer:\n"))
if distance <= 200:
    ticket = 0.5 * distance
else:
    ticket = 0.35 * distance 
print(f"Preço da passagem é {ticket:.2f}")

# 2 - Aumento salario funcionario
salary = float(input("Digite o seu salario:\n"))
perc_increase = 0.15

if salary > 1250:
    perc_increase = 0.10
increase = salary * perc_increase
print(f"Seu aumento sera de {increase:.2f}")