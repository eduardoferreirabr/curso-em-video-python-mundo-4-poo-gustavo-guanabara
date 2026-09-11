from classes import *


def main():
    a = Porta()
    b = Empresa()
    c = Ovo()
    d = Pedra()

    tentar_abrir(a)
    tentar_abrir(b)
    tentar_abrir(c)
    tentar_abrir(d)  # Vai dar erro, pois a classe Pedra não tem o método abrir()


if __name__ == "__main__":
    main()
