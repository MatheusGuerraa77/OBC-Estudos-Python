class Movie:
    def __init__(self, name, yearlaunch, includePlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearlaunch
        self.includePlan = includePlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0
        
    def __str__(self):
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("##Dados do Filme##")
        print(f"Nome do filme : {self.name}")
        print(f"Ano de lançamento : {self.yearLaunch}")
        print(f"Está no plano : {self.includePlan}")
        print(f"Avaliação do filme : {self.totalEvaluation}")
        print(f"Duração do filme : {self.durationMinutes}")
        print(f"Total Avaliadores: {self.evaluators}\n")
       
    def evaluate(self, note):
        self.totalEvaluation += note # totalEvaluation = totalEvaluation + note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators}\n")
        
mario = Movie("Super Mario Bross", 2023, False, 135)
avatar = Movie("Avatar", 2023, False, 180)
mario.evaluate(9.5)
mario.evaluate(10.0)
mario.techinal_sheet()
mario.average()
avatar.evaluate(8.5)
avatar.evaluate(9)
avatar.techinal_sheet()
avatar.average()