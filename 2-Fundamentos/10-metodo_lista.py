filmsList = ["Inception", "The Shawshank Redemption",
             "The Dark Knight", "Pulp Fiction",
             "Interstellar"]

# 0 - Encontrar o título de um filme pelo índice
filme_indice_0 = filmsList[0]
print(f"O filme no indice 0 é: {filme_indice_0}")

# 1 - Tamanho da Lista
numeroDeFilmes = len(filmsList)
print(f"A lista contém {numeroDeFilmes} filmes")

# 2 - Recuperar o índice de um filme pelo título

indiceDeInterstellar = filmsList.index("Interstellar")
print(f"O indice do filme Interstellar é {indiceDeInterstellar} ") 

# 3 - Adicionar item ao final da lista
filmsList.append("The Lord of the Rings")
print(filmsList)

# 4 - Ordenar a lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print(filmsCopy)

# 6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)