# crie classes capazes de calcular fretes de veículos diferentes.

# superclasse
# | Transporte {abstract}     |
# -----------------------------
# | **Atributos**             |
# | + distancia               |
# | + frete                   |
# -----------------------------
# | **Métodos**               |
# | + calc_frete() {abstract} |

# subclasse
# | Moto            |
# -------------------
# | **Atributos**   |
# | + fator = 0.50  |
# -------------------
# | **Métodos**     |
# | + calc_frete()  |

# subclasse
# | Caminhao        |
# -------------------
# | **Atributos**   |
# | + fator = 1.20  |
# -------------------
# | **Métodos**     |
# | + calc_frete()  |

# subclasse
# | Drone           |
# -------------------
# | **Atributos**   |
# | + fator = 9.50  |
# -------------------
# | **Métodos**     |
# | + calc_frete()  |

# moto: frete é livre
# caminhão: frete mínimo de 50 km
# drone: máximo 10 km
#
# o fator é um multiplicador (fator x km)

from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0  # Transporte.calc_frete(self)

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = Moto.fator * self.distancia
        return f"R$ {self.frete}"


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = f"R$ {Caminhao.fator * self.distancia}"
        else:
            self.frete = "Raio mínimo de 50 Km"
        return self.frete


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia <= 10:
            self.frete = f"R$ {Drone.fator * self.distancia}"
        else:
            self.frete = f"Raio máximo de 10 Km"
        return self.frete


dist = 80
# entrega = Moto(dist)
# print(f"Frete de {type(entrega).__name__} em {dist} Km = {entrega.calc_frete()}")

tam_coluna = 15

print(f"{'Tabela de Fretes':^{tam_coluna * 3}}")
print("-" * tam_coluna * 3)
print(f"{'Distância':<{tam_coluna}}", f"{'Tipo':<{tam_coluna}}", "Frete")
print("-" * tam_coluna * 3)


viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

for item in viagem:
    print(
        f"{dist:<{tam_coluna}}",
        f"{type(item).__name__:<{tam_coluna}}",
        item.calc_frete(),
    )
