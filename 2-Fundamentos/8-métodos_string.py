movieName = "Top Gun"

movieDescription = """
    Top Gun Maverick, é um filme de aviação e aventura, muito consagrado na indústria
"""

#tudo maiúsculo
print(movieName.upper())
#tudo minúsculo
print(movieName.lower())
# Primeira letra maiúscula
print(movieName.capitalize())
#Primeira letra de cada palavra
#maiúsculas
print(movieName.title())
#Retorna string centralizada
#com caractere de preenchimento
print(movieName.center(20, "-"))
#Retorna a posição da letra "u"
print(movieName.find("u"))
print(movieName.count("o"))
#Alterar elemento
#por outro
print(movieName.replace("Top", "Matrix"))
print(movieDescription.split(','))