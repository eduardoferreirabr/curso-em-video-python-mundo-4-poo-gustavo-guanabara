from classes import *


def main():
    c1 = Carteira(1000)
    c2 = Carteira(2000)

    c1 += 50
    c1 -= 10

    if c1 == c2:
        print("Vocês tem o mesmo valor na carteira.")
    else:
        print("As carteiras tem valores diferentes.")

    if c1 <= c2:
        print("A segunda carteira tem mais dinheiro.")
    else:
        print("A primeira carteira tem mais dinheiro.")
    print(c1)
    print(c2)


if __name__ == "__main__":
    main()
