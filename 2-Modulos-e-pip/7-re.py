import re
text = "Onebitcode: Transformamos pessoas em programadores sem limites"
# 1 - Indice inicial e final de palavras
# O r significa que estamos trabalhando com uma string bruta (raw String)
math = re.search(r'pessoas em programadores',text)
print('Indice inicial', math.start())
print('Indice final', math.end())

# 2 - Buscando o indice que possui o ponto
site = 'https://onebitcode.com'
#match = re.search(r'.', site)
match = re.search(r'\.', site)
print(match)

# 3 -Buscando uma Lista de caracteres dentro de uma frase
pattern = "[a-m]"
result = re.findall(pattern, text)
print(text)
print(result)

# 4 - Verificando o inicio de uma string
rule = r'^A'
phrases = ['A casa esta suja', 'O dia esta lindo', 'Vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f" Nao corresponde: {f}")

# 5 - Verificando o final de uma string
rule_end = r'!$'
phrases2 = 'O dia esta lindo!'
match = re.search(rule_end, phrases2)
if match:
    print(" Sim, Correponde")
else:
    print(" Não Corresponde")
    