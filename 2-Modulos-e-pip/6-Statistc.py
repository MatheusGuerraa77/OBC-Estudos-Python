import statistics

# 1 -aplicar a media
print(statistics.mean([3, 2, 3, 8, 9]))

# 2 - Calcular a mediana
print(statistics.median([1, 2, 3, 8, 9]))
print(statistics.median([1, 2, 3, 7, 8, 9]))


# 3 -Aplicar a moda 
print(statistics.mode([2, 5, 3, 2, 8, 3, 9, 4, 2, 5, 6]))

# 4 - Desvio padrao
"""
-Quanto mais proximo de 0 for o desvio padrao,
significa que os dados do conjunto estao menos dispersos

"""
print(statistics.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]))