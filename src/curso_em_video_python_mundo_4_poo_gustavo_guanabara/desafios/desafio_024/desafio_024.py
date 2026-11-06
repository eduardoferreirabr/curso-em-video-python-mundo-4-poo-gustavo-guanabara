# simule uma cafeteira orientada a objetos

# superclasse
# | BebidaQuente {abstract}    |
# ----------------------------
# ----------------------------
# | **Métodos**                |
# | + preparar()               |
# | + ferver_agua()            |
# | + misturar() {abstract}    |
# | + servir() {abstract}      |

# subclasse
# | Café          |
# -----------------
# -----------------
# | **Métodos**   |
# | + misturar()  |
# | + servir()    |

# subclasse
# | Cha           |
# -----------------
# -----------------
# | **Métodos**   |
# | + misturar()  |
# | + servir()    |

# subclasse
# | Leite         |
# -----------------
# -----------------
# | **Métodos**   |
# | + misturar()  |
# | + servir()    |

# ------------------------------------------------------

# Para café:
# bebida = Cafe()
# bebida.preparar()
#
# --- Iniciando o Preparo ---
# 1. Fervendo água a 100 graus Celsius.
# 2. Passando água pressurizada pelo pó de café moído.
# 3. Servindo em xícara pequena.
# --- Bebida Pronta ---

# Para chá:
# bebida = Cha()
# bebida.preparar()
#
# --- Iniciando o Preparo ---
# 1. Fervendo água a 100 graus Celsius.
# 2. Mergulhando o sachê de ervas na água.
# 3. Servindo na caneca de porcelana com limão.
# --- Bebida Pronta ---

# Para leite:
# bebida = Leite()
# bebida.preparar()
#
# --- Iniciando o Preparo ---
# 1. Fervendo água a 100 graus Celsius.
# 2. Passando vapor pressurizado pelo bico do leite.
# 3. Servindo na caneca grande, já com café.
# --- Bebida Pronta ---

from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def preparar(self):
        print("--- Iniciando o Preparo ---")
        print(self.ferver_agua())
        print(self.misturar())
        print(self.servir())
        print("--- Bebida Pronta ---\n\n")

    def ferver_agua(self):
        return "1. Fervendo água a 100 graus Celsius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        return "2. Passando água pressurizada pelo pó de café moído."

    def servir(self):
        return "3. Servindo em xícara pequena."


class Cha(BebidaQuente):
    def misturar(self):
        return "2. Mergulhando o sachê de ervas na água."

    def servir(self):
        return "3. Servindo na caneca de porcelana com limão."


class Leite(BebidaQuente):
    def misturar(self):
        return "2. Passando vapor pressurizado pelo bico do leite."

    def servir(self):
        return "3. Servindo na caneca grande, já com café."


print("Café:")
bebida = Cafe()
bebida.preparar()

print("Chá")
bebida = Cha()
bebida.preparar()

print("Leite")
bebida = Leite()
bebida.preparar()
