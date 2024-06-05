class Animal:
    name = ""
    size = ""
    color = ""

    def eat(self):
        print("Animal se alimentando")
        
class Horse(Animal):
    race = ""
    
    def escape(self):
        print("Cavalo fugindo")
        
class Lion(Animal):
    name = True
    
    def hunt(self):
        print("Leão caçando")
        
h = Horse()
h.name = "Carpeado"
h.color = "Branco"
h.escape()
h.eat()

l = Lion()
l.name = "Simba"
l.color = "marrom"
l.hunt()
l.eat()