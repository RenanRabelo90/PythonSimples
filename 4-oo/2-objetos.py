class Game:
    def __init__(self, name="", releaseYear=0, multiplayer=False, score=0):
        self.name = name
        self.releaseYear = releaseYear
        self.multiplayer = multiplayer
        self.score = score
    def __str__(self):
        return f"Game: {self.name}"

# Primeiro jogo
game1 = Game()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.releaseYear = 2017
game1.multiplayer = False
game1.score = 9.5

# Segundo Jogo
game2 = Game("Fornite", 2017, True, 8.0)

# Terceiro Jogo
game3 = Game("Diablo IV", 2023, True, 7.6)

# Quarto Jogo
game4 = Game("Age of Mythology: Retold", 2024, True, 9.0)

def printar(game):
    print("###Dados do Jogo###")
    print(f"Nome do jogo: {game.name}")
    print(f"Ano de lançamento: {game.releaseYear}")
    print(f"Multiplayer: {game.multiplayer}")
    print(f"Nota do game: {game.score}\n ")

printar(game1)
printar(game2)
printar(game3)
printar(game4)