class employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        
    def show(self):
        print(f"Nome {self.name} - Salário {self.__salary}")
        
    #Método para buscar dados
    def get_salary(self):
        return self.__salary
    
    #Método para modificar atributo privado
    def set_salary(self, salary):
        self.__salary = salary
        
fulano = employee("Fulano",4000)
sícrano = employee("Sícrano",7000)
fulano.name = "Fulano 2"
fulano.show()
sícrano.show()
fulano.set_salary(10000)
fulano.show()