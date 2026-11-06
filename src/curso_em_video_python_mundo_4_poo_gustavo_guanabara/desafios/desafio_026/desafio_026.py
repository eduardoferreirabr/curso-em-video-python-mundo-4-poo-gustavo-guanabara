# crie uma estrutura capaz de calcular salários de funcionários diferentes

# superclasse
# | Funcionario {abstract}  |
# ---------------------------
# | **Atributos**           |
# | + nome                  |
# | + sal_bruto             |
# | + salario               |
# | + sal_min = 1612        |
# | + inss = 7.5            |
# ---------------------------
# | **Métodos**             |
# | + calc_sal() {abstract} |
# | + analisar_sal          |

# subclasse
# | Horista       |
# -----------------
# | **Atributos** |
# | + valor_hora  |
# | + horas_trab  |
# -------------------
# | **Métodos**   |
# | + calc_sal()  |

# subclasse
# | Mensalista    |
# -----------------
# -----------------
# | **Métodos**   |
# | + calc_sal()  |

from abc import ABC, abstractmethod


class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        texto = (
            f"O salário de {self.nome} ({self.__class__.__name__}) é de "
            f"R$ {self.salario:.2f} e corresponde "
            f"a {self.salario / Funcionario.sal_min:.1f} salários mínimos."
        )

        return texto


class Horista(Funcionario):
    def __init__(self, nome, valor_hora=7.37, horas_trab=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calc_sal(self):
        self.salario = self.sal_bruto * (1 - Funcionario.inss / 100)
        return self.salario


class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto=Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto * (1 - Funcionario.inss / 100)
        return self.salario


f1 = Horista("Maria de Souza", 25, 250)
f1.calc_sal()
print(f1.analisar_sal())

f2 = Mensalista("josé da Silva", 8500)
f2.calc_sal()
print(f2.analisar_sal())
