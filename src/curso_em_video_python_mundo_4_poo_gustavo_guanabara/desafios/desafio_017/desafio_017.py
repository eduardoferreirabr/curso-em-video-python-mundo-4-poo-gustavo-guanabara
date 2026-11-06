# Desafio 017
# crie a classe Produto, onde podemos cadastrar nome e preço.
# crie também um método que mostra uma etiqueta de preço do produto.


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return f"{self.nome} --- {self.preco}"


p1 = Produto("iphone 17 pro max", "R$ um zilhão")
print(p1.etiqueta())

p2 = Produto("samsung mais em conta", "R$ custo beneficio")
print(p2.etiqueta())
