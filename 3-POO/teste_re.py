import re

def from_text(string):
    item = re.findall("é \w*", string)
    return item[1][2:]

print(from_text("Meu vídeo game é WiiU e o preço é 1000 reais"))