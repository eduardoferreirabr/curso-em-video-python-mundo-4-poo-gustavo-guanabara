class Numero:
    def __init__(self, valor: int | float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f"Tenho o número {self.valor} dentro do número"


class Texto:
    def __init__(self, txt: str = ""):
        self.texto = txt

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do texto"


class Lista:
    def __init__(self, lst: list = []):
        self.valores = lst

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
        return f"Tenho a lista {self.valores} dentro da lista"


class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel está {'novo' if not self.dobrado else 'dobrado'}"


class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa muito engraçada, não tinha teto, não tinha nada"


# DUCK TYPING


def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Tive dificuldades para dobrar o {objeto.__class__.__name__}")
