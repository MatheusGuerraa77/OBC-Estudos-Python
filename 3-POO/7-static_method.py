"""

1- O método estático não utiliza o parâmetro referente a classe,
2- O método estático pode acessar mas não pode modificar o estado da classe.
3- Utilizamos o decorator @sthaticmethod para criar um método de classe
"""

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail
        
    @staticmethod
    def courses_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python", "Módulos e Pip", "Orientação a Objetos"]
        elif trail == "Automação com o Python":
            courses = ["Automação de tarefas", "Web Scraping","Assistente Virtual em python"]
        else:
            courses = ["A definir"]
        return courses
    
print(Course.courses_trail("Python Fundamentos"))
print(Course.courses_trail("Análise de dados"))
print(Course.courses_trail("Automação com o Python"))
        
        