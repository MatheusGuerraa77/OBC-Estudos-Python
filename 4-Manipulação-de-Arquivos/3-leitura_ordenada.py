names = []

with open("dados/names.txt", "r", encoding="utf8") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"Olá, {name}") 
    