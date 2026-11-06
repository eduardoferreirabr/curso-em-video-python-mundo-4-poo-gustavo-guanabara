# Desafio 020
# crie uma classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# crie também um método que permita mostrar a ficha desse gamer.


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, *game):
        self.favoritos.append(game)

    def mostrar_ficha(self):
        print(f"{self.nome}")
        print(f"{self.nick}\n")
        for games in self.favoritos:
            for game in games:
                print(f"{game}")


g1 = Gamer("Edu", "DuDudueEdu")
g1.add_favoritos("God of War")
g1.add_favoritos("Prince of Persia")
g1.add_favoritos("Need for Speed")
g1.add_favoritos("Mario Kart", "Super Mario")
g1.mostrar_ficha()
