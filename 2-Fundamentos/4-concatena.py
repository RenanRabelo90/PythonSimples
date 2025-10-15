name = input("Digite o nome do filme:\n")
releaseYear = int(input("digite o ano de lançamento do filme:\n"))
movieScore = float(input("Digite a nota do filme:\n"))

#Alternativa 1
# print("Dados do Filme")
# print("************")
# print("Nome do filme:", name)
# print("Ano de lançamento:", releaseYear)
# print("Nota do filme:", movieScore)

#Alternativa 2
#print("Nome do Filme:", name, "\nAno de Lançamento:", releaseYear, "\nNota do Filme:", movieScore)

#Alternativa 3
print(f"Nome do Filme: {name}\n"
      f"Ano de Lançamento: {releaseYear}\n"
      f"Nota do filme: {movieScore}") 