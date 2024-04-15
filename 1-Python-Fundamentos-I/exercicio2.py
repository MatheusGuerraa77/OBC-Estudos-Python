# * Substituindo caractere repetido :
name = "Fifa 23"
char = name[0].lower()
new = name.replace(char, '$')
new = char +  new[1:]
print(new)

#Troca de caracteres:

st1 = "cab" #zyb
st2 = "zyx" #cax
new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print(f"{new_st1} {new_st2}")