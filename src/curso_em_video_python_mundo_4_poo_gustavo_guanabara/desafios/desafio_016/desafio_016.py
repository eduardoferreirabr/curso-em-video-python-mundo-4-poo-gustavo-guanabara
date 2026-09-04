# crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
# crie também um método que permita ao funcionário se apresentar.
from rich import inspect


class Funcionario:
    # atributos de classe
    empresa = "Curso em Video"

    # atributos de instancia
    def __init__(self, nome, setor, cargo):
        # atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f"Meu nome é {self.nome}, trabalho no setor {self.setor} e possuo o cargo de {self.cargo} da empresa {Funcionario.empresa}.\n"


f1 = Funcionario("Jurandir", "Automobilistico", "Piloto")
print(f1.apresentar())

f2 = Funcionario("José", "Pai de Jesus", "Marceneiro")
print(f2.apresentar())

inspect(f1)
print(f1.__dict__)
print(f1.setor)
print(f2.nome)
