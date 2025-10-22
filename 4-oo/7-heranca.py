# Classe pai/mãe (Super classe) - Classe generalista
class Game:
    total_games = 0
    def __init__(self, name="", releaseYear=0, multiplayer=False, score=0):
        self.name = name
        self.releaseYear = releaseYear
        self.multiplayer = multiplayer
        self.score = score
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
        
    def __str__(self):
        return f"Game: {self.name}"
        
    # CORREÇÃO: Método técnico da classe pai. Imprime todos os dados BÁSICOS e
    # adiciona a linha em branco de SEPARAÇÃO.
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.releaseYear}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.score}") 
        # Linha em branco para separar esta ficha técnica da próxima (game2, game3, game4)
        print() 
        
    def evaluate(self, score):
        self.totalEvaluation += score
        self.evaluators += 1
        
    def average(self):
        if self.evaluators > 0:
            print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators:.2f}")
        else:
            print(f"Média do jogo {self.name}: Nenhuma avaliação realizada.")

# Classe derivada (Subclasse) - Classe especializada
class SinglePlayerGame(Game):
    def __init__(self, name="", releaseYear=0, score=0, storyline=""):
        super().__init__(name, releaseYear, multiplayer=False, score=score)
        self.storyline = storyline

    # Sobrescrita do método
    def technical_sheet(self):
        # 1. Imprime os dados básicos (Score incluído), mas sem a linha em branco final
        # Note que precisamos REPETIR o código da classe pai, pois não queremos a linha em branco de lá.
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.releaseYear}")
        print(f"Multiplayer: {self.multiplayer}")
        # AVALIAÇÃO + QUEBRA DE LINHA SIMPLES
        print(f"Avaliação do Jogo: {self.score}") 
        
        # 2. Imprime o Enredo na linha seguinte
        # AQUI COLOCAMOS A LINHA EM BRANCO PARA SEPARAR esta ficha da próxima.
        print(f"Enredo> {self.storyline}\n") 


# Primeiro jogo
game1 = SinglePlayerGame()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.releaseYear = 2017
game1.score = 9.5
game1.storyline = "Emocionante história de aventura e sobrevivência"

# Segundo Jogo
game2 = Game("Fornite", 2017, True, 8.0)

# Terceiro Jogo
game3 = Game("Diablo IV", 2023, True, 7.6)

# Quarto Jogo
game4 = Game("Age of Mythology: Retold", 2024, True, 9.0)


# -----------------
# Chamadas dos métodos
# -----------------
game1.technical_sheet() 
game2.technical_sheet() 
game3.technical_sheet() 
game4.technical_sheet() 


game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)

game1.average()
game2.average()

# Exibindo o número total de jogos criados
print(f"\nTotal de jogos criados: {Game.total_games}")


# Primeiro jogo
game1 = SinglePlayerGame()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.releaseYear = 2017
game1.score = 9.5
game1.storyline = "Emocionante história de aventura e sobrevivência"

# Segundo Jogo
game2 = Game("Fornite", 2017, True, 8.0)

# Terceiro Jogo
game3 = Game("Diablo IV", 2023, True, 7.6)

# Quarto Jogo
game4 = Game("Age of Mythology: Retold", 2024, True, 9.0)


# -----------------
# Chamadas dos métodos
# -----------------
game1.technical_sheet() # Chama subclasse: quebra de linha única entre score e enredo
game2.technical_sheet() # Chama classe pai: quebra de linha dupla (simples + print padrão)
game3.technical_sheet() # Chama classe pai: quebra de linha dupla
game4.technical_sheet() # Chama classe pai: quebra de linha dupla


game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)

game1.average()
game2.average()

# Exibindo o número total de jogos criados
print(f"\nTotal de jogos criados: {Game.total_games}")