produto1 = input("Insira o nome do 1º produto.\n")
preco1 = float(input("Insira o preço do 1º produto.\n"))
produto2 = input("Insira o nome do 2º produto.\n")
preco2 = float(input("Insira o preço do 2º produto.\n"))
produto3 = input("Insira o nome do 3º produto.\n")
preco3 = float(input("Insira o preço do 3º produto.\n"))

dictProdutos = {produto1: preco1,
                produto2: preco2,
                produto3: preco3
}


print(dictProdutos)

produto_mais_caro = max(dictProdutos.items(), key=lambda item: item[1])

print(produto_mais_caro[0])

#Calcula a média dos preços
# Acessa apenas os valores (preços) do dicionario
lista_precos = dictProdutos.values()
soma_precos = sum(lista_precos)
quantidade = len(dictProdutos)

#media = soma / quantidade
media_precos = soma_precos / quantidade

print(f"{media_precos:.2f}")