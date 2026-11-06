# simule o sistema de batalha entre personagens de um RPG

# superclasse
# | Personagem {abstract}
# -------------------------
# | **Atributos**         |
# | + nome                |
# | + vida                |
# | + golpes              |
# -------------------------
# | **Métodos**           |
# | + atacar(alvo, forca) |
# | + receber_dano(dano)  |
# | + curar {abstract}    |

# subclasse
# | Guerreiro            |
# ------------------------
# ------------------------
# | **Métodos**          |
# | + curar() |

# subclasse
# | Mago                 |
# ------------------------
# ------------------------
# | **Métodos**          |
# | + curar()            |

from abc import ABC, abstractmethod
from random import choice, randint


class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = [
            "Golpe de Machado",
            "Cacetete do Policial",
            "Magia do Doutor Estranho",
            "Pulo Giratório",
        ]

    def atacar(self, Personagem):
        golpe = choice(self.golpes)
        tam_forca = randint(100)
        tam_dano = randint(100)

        ataque = f"{self.nome}({self.vida}) atacou {Personagem.nome}({Personagem.vida}) com um {golpe} de força {tam_forca}."
        receba = self.receber_dano(Personagem, tam_dano)

        Personagem.vida = Personagem.vida - tam_dano

        print(ataque)
        print(receba)

    def receber_dano(self, Personagem, tam_dano):
        return f"{Personagem.nome} recebeu dano de {tam_dano}!"

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        tam_cura = choice(range(100))
        self.vida = self.vida + tam_cura
        print(
            f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {tam_cura} de vida."
        )


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        tam_cura = choice(range(100))
        self.vida = self.vida + tam_cura
        print(f"{self.nome} fez uma magia de cura e recuperou {tam_cura} de vida.")


p1 = Guerreiro("Megaman", 1000)
p2 = Mago("Merlin", 5000)
p3 = Guerreiro("Kratos", 1500)

p1.atacar(p2)
p1.atacar(p2)
p3.atacar(p1)

p2.curar()
p1.curar()

print(f"{p1.nome}: {p1.vida}")
print(f"{p2.nome}: {p2.vida}")
