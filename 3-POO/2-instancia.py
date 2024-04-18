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


print("##Dados do Filme##")
print(f"Nome do filme : {movie.name}  \n Ano de lançamento: {movie.yearLaunch}")