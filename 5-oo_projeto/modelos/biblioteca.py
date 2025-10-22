from modelos.itens.item_biblioteca import ItemBiblioteca

from modelos.avaliacao import Avaliacao 
# from modelos.itens.item_biblioteca import ItemBiblioteca # Linha original

# ----------------------------------------

class Biblioteca:
    bibliotecas =[]
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False
        self._avaliacao = []
        self._itens =[]
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_bibliotecas(cls):
        print(f"\n{'Nome da biblioteca'.ljust(25)} | {'Nota media'.ljust(15)} | {'Status'}")
        print('-' * 55)
        for biblioteca in Biblioteca.bibliotecas:
            # Garante que a média seja formatada como string
            media_str = str(biblioteca.media_avaliacoes).ljust(15)
            print(f"{biblioteca.nome.ljust(25)} | {media_str} | {biblioteca.ativo}")
        print(f"\nO número atual de bibliotecas cadastradas é {len(Biblioteca.bibliotecas)}")

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativa" if self._ativo else "inativa"
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma / len(self._avaliacao), 1)
        return media

    def adicionar_item(self, item):
        # Verifica se o item é uma instância da classe base ItemBiblioteca ou suas subclasses
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)
    
    def exibir_itens(self):
        print(f"\n--- Itens da Biblioteca: {self.nome} (Total: {len(self._itens)}) ---")
        if not self._itens:
             print("Nenhum item cadastrado.")
             return
             
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, 'isbn'):
                # Assumimos que 'isbn' só existe em Livro (subclasse de ItemBiblioteca)
                msg_livro = f"{i}. (Livro) -> Título: {item._titulo} | Autor: {item._autor} | Preço: R${item._preco:.2f} | ISBN: {item.isbn}"
                print(msg_livro)
            elif hasattr(item, 'edicao'):
                # Assumimos que 'edicao' só existe em Revista (subclasse de ItemBiblioteca)
                msg_revista = f"{i}. (Revista) -> Título: {item._titulo} | Autor: {item._autor} | Preço: R${item._preco:.2f} | Edição: {item.edicao}"
                print(msg_revista)
            else:
                 # Caso seja um ItemBiblioteca genérico sem ISBN/Edição
                 msg_generico = f"{i}. (Item Genérico) -> Título: {item._titulo} | Preço: R${item._preco:.2f}"
                 print(msg_generico)

    # CORREÇÃO: Método que lista a tabela e, em seguida, chama exibir_itens
    @classmethod
    def listar_tudo(cls):
        print("\n*** RELATÓRIO COMPLETO DAS BIBLIOTECAS ***")
        
        # 1. Exibe a tabela de bibliotecas
        cls.listar_bibliotecas() 
        
        # 2. Exibe os itens de cada biblioteca
        for biblioteca in Biblioteca.bibliotecas:
            # CORREÇÃO: Chama o método de instância corretamente
            biblioteca.exibir_itens() 




# Listar TUDO

# print vars retorna a biblioteca como 
# um dicionário

