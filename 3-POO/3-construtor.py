class Movie:
    def __init__(self, name, yearlaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearlaunch
        self.includePlan = includePlan
        self.note = note
        self.durationMinutes = durationMinutes
        
    def __str__(self):
        return f"Filme: {self.name}"
        
movie = Movie("Super Mario Bros", 2023, False, 5.0, 130)
movie2 = Movie("Avatar", 2023, False, 4.5, 220)

print("##Dados do filme##")
print(movie.name,
      movie.yearLaunch, 
      movie.includePlan, 
      movie.note, 
      movie.durationMinutes)
print("##Dados do Filme2##")
print(movie2.name,
      movie2.yearLaunch, 
      movie2.includePlan, 
      movie2.note, 
      movie2.durationMinutes)
print("##Nome do FIlme##")
print(movie)
print("##Nome do FIlme2##")
print(movie2)