# Desafio 018
# crie uma classe Churrasco, onde seja possível informar quantas pessoas vão participar e
# mostre quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.

# considere:
# consumo padrão: 400g/pessoa
# preço: R$ 82,40/Kg


class Churrasco:
    # atributos de classe
    consumo_padrao = 0.400  # cada pessoa consome em média 400g de carne
    preco_por_kg = 82.40

    # atributos de instancia
    def __init__(self, quant_pessoas):
        # atributos de instancia
        self.quant_pessoas = quant_pessoas

    # métodos de instancia
    def calcular_qtd_carne(self) -> float:
        return self.quant_pessoas * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_por_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quant_pessoas

    def analisar(self):
        qtd_carne = f"Recomendo comprar {self.calcular_qtd_carne():.2f} kg de carne."
        custo_total = f"O custo total será de R$ {self.calcular_custo_total():.2f}."
        custo_individual = (
            f"O custo individual será de R$ {self.calcular_custo_individual():.2f}."
        )
        return qtd_carne, custo_total, custo_individual


c1 = Churrasco(15)
for i in c1.analisar():
    print(i)
