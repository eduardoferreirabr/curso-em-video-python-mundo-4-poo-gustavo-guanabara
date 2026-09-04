class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(
            f"Conta {self.id} criada com sucesso. Saldo atual de R$ {self.saldo:,.2f}"
        )

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito autorizado de R$ {valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(
                f"Saque NEGADO de R$ {valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE"
            )
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:,.2f} autorizado na conta {self.id}")


c1 = ContaBancaria(112, "Gustavo", saldo=3000)

c1.depositar(500)
c1.sacar(2_000_000)


print(c1)
print(c1.__doc__)
