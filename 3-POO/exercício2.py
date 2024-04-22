class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"Produto : {self.name} - R$ {self.price} reais"
    
    def discount(self, perc_discount):
        valorDiscount = (self.price/100) * perc_discount
        finalPrice = self.price - valorDiscount
        return int(finalPrice)
    
xbox = Product("Xbox Series X", 4500)
iphone = Product("Iphone 14 Pro", 7500)
print(xbox)
print(iphone)
print(xbox.discount(10))
print(iphone.discount(15))