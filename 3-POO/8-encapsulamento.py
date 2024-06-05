class employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")
        
fulano = employee("Fulano", 4000)
sícrano = employee("Sícrano", 5000)
fulano.show()
sícrano.show()
fulano.__salary = 4000
fulano.show()
