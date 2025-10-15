# Utilizando o Input


name =input("Digite o nome do filme:\n")
releaseYear = int(input("digite o ano de lançamento do filme:\n"))
movieScore = float(input("Digite a nota do filme:\n"))

print(f"Nome: {name} | Tipo: {type(name).__name__}" )
print(f"Ano de Lançamento: {releaseYear} | Tipo: {type(releaseYear).__name__}")
print(f"Nota do Filme: {movieScore} | Tipo: {type(movieScore).__name__}")


