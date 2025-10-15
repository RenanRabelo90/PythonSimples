#O Python é case sensitive

movieName = "   Top Gun"
movieName2 = "top Gun"

print(f"Filme 1 é igual ao Filme 2? {movieName == movieName2}")

# 0 - String multilinhas

movieDescription = """
    Top Gun Maverick é um
    filme de aviação e aventura
    muito consagrado na indústria
"""


print(movieName)
# 1- Multiplicação de Strings
line = "="
print (line*50)
print(movieDescription)

# 2 - Procurar uma palavra dentro de um texto
print ("top" in movieName)
print("Top" in movieName)
print("ação" in movieName)