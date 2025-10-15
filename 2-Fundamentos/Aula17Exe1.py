#1 - Escreva um programa que lê 
# dois nomes e retorne uma string
# formatada no formato 
# "Último Nome, Primeiro Nome"

#2- Inverta a ordem das palavras
# em uma string fornecida.

#3- Verifique se uma string
#fornecida é um palíndromo
#(pode ser lida da mesma forma
#de trás para frente)

#1
primNome = input("escreva o primeiro nome.\n")
ultNome = input("escreva o último nome.\n")

print(f"{ultNome}, {primNome}")
print(f"{primNome}, {ultNome}")

#2
texto = "Python é muito interessante"
#dividir o texto separando em
#strings a cada espaço vazio
# espaço vazio = argumento
#do split
palavras = texto.split() 
textoInvertido = " ".join(palavras[::-1])
print(textoInvertido)

#3
palavra = input("escreva uma palavra.\n")
palavra_format = palavra.lower().replace(" ", "")
if palavra_format[0:] == palavra_format[::-1] :
    print(f"a palavra {palavra} é um palíndromo")
else :
    print(f"a palavra {palavra} não é um palíndromo")
