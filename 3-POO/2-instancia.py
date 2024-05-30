class Movie:
    name = ""
    yearLaunch = 0
    included = False
    note = 0
    durationMinutes = 0
    
# Primeiro filme #
movie = Movie()
movie.name = "Super Mario Bross"
movie.yearLaunch = 2023
movie.viewincluded = False
movie.note = 5.0
movie.durationMinutes = 130

#Segundo filme
movie2 = Movie()
movie2.name = "Kung Fu Panda 4"
movie2.yearLaunch = 2024
movie2.included = False
movie2.note = 7.0
movie2.durationMinutes = 90




print("##Dados do Filme##")
print(f"Nome do filme : {movie.name}  \n Ano de lançamento: {movie.yearLaunch}")
print("##Dados do Filme 2##")
print(f"Nome do filme : {movie2.name}  \n Ano de lançamento: {movie2.yearLaunch}")