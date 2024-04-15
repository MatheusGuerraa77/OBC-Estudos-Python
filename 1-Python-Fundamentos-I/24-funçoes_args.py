"""
*args - Utilizamos ele quando nao temos certeza de quantos argumentos
queremos ter num funçao.
- Os argumentos sao passados como uma tupla


**kwargs - Alem dos valores podemos passar tambem as respectivas chaves para cada argumento.
- Os argumentos sao passados com um dicionario
"""

# 1 - Soma de numeros
def sum(*num):
    sum_total = 0
    for n in num: #laço de repetiçao
        sum_total += n # sum_total = sum_total  + n
    print(f"Soma é : {sum_total}\n")

sum(7)
sum(7,9)
sum(7, 9, 10, 11)
sum(7, 10, 9, 8, 7, 6)

# 2 - Apresentaçao de cursos

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")

print("###Curso###\n")
presentation(name ="Python", category = "backend", Level = "iniciante\n")
presentation(name ="Visao Computacional com Python", category = "IA", Level = "Avançado\n")
presentation(name ="Dashboards com Dash", category = "Data Science", Level = "Intermediario\n")