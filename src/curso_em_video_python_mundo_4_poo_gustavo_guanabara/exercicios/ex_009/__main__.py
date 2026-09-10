from ex_009 import Avaliacao
from rich import inspect, print


def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    av1.set_nota(10)
    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}")
    inspect(av1, private=True)


if __name__ == "__main__":
    main()
