listaDeNumeros = []

primeiro = int(input("Digite o primeiro número.\n"))
listaDeNumeros.append(primeiro)
segundo = int(input("Digite o segundo número.\n"))
listaDeNumeros.append(segundo)
terceiro = int(input("Digite o terceiro número.\n"))
listaDeNumeros.append(terceiro)
quarto = int(input("Digite o quarto número.\n"))
listaDeNumeros.append(quarto)
quinto = int(input("Digite o quinto número.\n"))
listaDeNumeros.append(quinto)

setDeNumeros = set(listaDeNumeros)
#O Set resultante
print(setDeNumeros)

#A quantidade de elementos únicos
print(len(setDeNumeros))

#O maior elemento do set
maior_elemento = max(setDeNumeros)
print(maior_elemento)