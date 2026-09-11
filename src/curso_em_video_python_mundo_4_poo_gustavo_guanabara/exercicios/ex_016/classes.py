class Porta:
    def abrir(self):
        print("Girar a maçanet e empurar/puxar a porta")


class Empresa:
    def abrir(self):
        print("Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ")


class Ovo:
    def abrir(self):
        print("Quebre a casca com um garfo e separe as partes sobre uma frigideira")


class Pedra:
    pass


# MÉTODO PYTHONICO POLIMÓRFICO DUCK TYPING


def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(
            f"Encontrei problemas ao tentar abrir um objeto tipo {objeto.__class__.__name__}"
        )
