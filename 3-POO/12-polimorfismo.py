class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        
    def __str__(self):
        return f"{self.brand}{self.model_name}"
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")
        
    def discount(self):
        return self.price * 0.10
        
class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
        
    def discount(self):
        return self.price * 0.15

Moto = Phone('Moto', 'G7', 1000)
print(Moto)
Moto.make_a_call(1312322)
print(f"Valor do {Moto.brand}{Moto.model_name} é {Moto.price}")
print(vars(Moto))   
print(Moto.discount())    
        
Iphone = SmartPhone("Iphone","13", 5000, "4GB", "128GB", "25MP")
print(Iphone)
Iphone.make_a_call(2433534)
print(f"Valor do {Iphone.brand}{Iphone.model_name} é {Iphone.price}")
print(vars(Iphone))  
print(Iphone.discount())      