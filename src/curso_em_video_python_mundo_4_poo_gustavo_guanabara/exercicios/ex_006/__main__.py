from aluno import Aluno
from funcionario import Funcionario
from professor import Professor
from rich import inspect


def main():
    a1 = Aluno("Jose", 17, "Informatica", "T01")
    a1.fazer_aniversário()
    a1.fazer_matricula()
    inspect(a1, methods=True)

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    p1.dar_aula()
    inspect(p1, methods=True)

    f1 = Funcionario("Claudia", 28, "Secretaria", "Secretaria")
    f1.bater_ponto()
    inspect(f1, methods=True)


if __name__ == "__main__":
    main()
