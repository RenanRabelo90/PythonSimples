from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista
from modelos.itens.item_biblioteca import ItemBiblioteca

biblioteca_cidade = Biblioteca("Biblioteca Municipal")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

# Adicionar itens à Biblioteca Municipal
livroC1 = Livro("1984", "George Orwell", 30.0, "084-3245")
livroC2 = Livro("A Arte da Guerra", "Sun Tzu", 35.00, "978-8578270275")
revistaC1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")
biblioteca_cidade.adicionar_item(livroC1)
biblioteca_cidade.adicionar_item(livroC2)
biblioteca_cidade.adicionar_item(revistaC1)
biblioteca_cidade.alterna_estado() # Ativa

livroC1.aplicar_desconto()
revistaC1.aplicar_desconto()

# Adicionar itens à Biblioteca do Shopping
livroS1 = Livro("Brave New World", "Aldous Huxley", 25.0, "084-1235")
livroS2 = Livro("Python para Iniciantes", "Guido", 80.00, "978-1234567890")
revistaS1 = Revista("Mundo Estranho", "Vários", 12.50, "Ed. 200")
biblioteca_shopping.adicionar_item(livroS1)
biblioteca_shopping.adicionar_item(livroS2)
biblioteca_shopping.adicionar_item(revistaS1)
biblioteca_shopping.alterna_estado() # Ativa

# Receber avaliações
biblioteca_cidade.receber_avaliacao("C1", 10)
biblioteca_cidade.receber_avaliacao("C2", 8)
biblioteca_shopping.receber_avaliacao("C3", 9.5)



def main():
    #Biblioteca.listar_bibliotecas()
    # print(vars(livro1))
    # print(vars(revista1))
    # biblioteca_cidade.exibir_itens()
    Biblioteca.listar_tudo()

if __name__ == "__main__":
    main()