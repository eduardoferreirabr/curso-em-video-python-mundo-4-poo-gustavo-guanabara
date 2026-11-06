# Desafio 023
# implemente o seguinte diagrama de classes

# superclasse
# | Poligono {abstract}      |
# ----------------------------
# | **Atributos**            |
# | + qtd_lados              |
# ----------------------------
# | **Métodos**              |
# | + perimetro() {abstract} |
# | + area() {abstract}      |

# subclasse
# | Quadrado                 |
# ----------------------------
# | **Atributos**            |
# | + lado                   |
# ----------------------------
# | **Métodos**              |
# | + perimetro()            |
# | + area()                 |

# subclasse
# | Circulo                  |
# ----------------------------
# | **Atributos**            |
# | + raio                   |
# ----------------------------
# | **Métodos**              |
# | + perimetro()            |
# | + area()                 |

import math
from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        perimetro = self.lado * 4
        return perimetro

    def area(self):
        area = self.lado**2
        return area


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        perimetro = round(2 * math.pi * self.raio, 2)
        return perimetro

    def area(self):
        area = round(math.pi * self.raio**2, 2)
        return area


p1 = Quadrado(12)
print(f"perimetro quadrado: {p1.perimetro()}")
print(f"area quadrado: {p1.area()}")

p2 = Circulo(1)
print(f"perimetro circulo: {p2.perimetro()}")
print(f"area circulo: {p2.area()}")

print(p2.qtd_lados)
