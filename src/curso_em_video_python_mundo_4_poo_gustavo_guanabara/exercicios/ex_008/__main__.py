from ex_008 import ContaBancaria


def main():
    c1 = ContaBancaria(111, "Maria", saldo=5_000)
    c1.depositar(1_000)
    c1._titular = "Pedro"

    c1._ContaBancaria__saldo = 0
    print(c1)


if __name__ == "__main__":
    main()
