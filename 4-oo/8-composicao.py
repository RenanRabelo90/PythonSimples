class Game:
    total_games = 0 # variável de classe para contar o número total 
    #de jogos
    def __init__(self, name="", releaseYear=0, multiplayer=False, score=0):
        self.name = name
        self.releaseYear = releaseYear
        self.multiplayer = multiplayer
        self.score = score
        Game.total_games +=1
        self.totalEvaluation = 0
        self.evaluators = 0
    def __str__(self):
        return f"Game: {self.name}"
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.releaseYear}")
        print(f"Multiplayer: {self.multiplayer}")
        print(f"Nota do game: {self.score} ")
        print(f"Avaliação do Jogo: {self.score}\n")

class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_score = sum(game.score for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estúdio {self.name} ainda não lançou jogo(s)")
        else:
            average_score = total_score / num_games
            print(f"A avaliação média dos jogos do estúdio {self.name} é: {average_score:.2f}\n")

game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("The Last of Us II", 2020, False, 9.0)

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()