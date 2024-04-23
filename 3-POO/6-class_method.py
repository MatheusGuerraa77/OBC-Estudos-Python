"""

1- O método de classe utiliza o parâmetro referente a classe,
2- O método de classe pode acessar ou modificar o estado da classe.
3- Utilizamos o decorator @classmethod para criar um método de classe
"""

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string):
        import re    
        item = re.findall("é \\w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))
    
WiiU = Console.from_text("Meu vídeo game é o WiiU e o preço é 1000 reais")
xboxOne = Console.from_text("Meu vídeo game é Xboxone e o preço é 1500 reais")
print(WiiU.__dict__)