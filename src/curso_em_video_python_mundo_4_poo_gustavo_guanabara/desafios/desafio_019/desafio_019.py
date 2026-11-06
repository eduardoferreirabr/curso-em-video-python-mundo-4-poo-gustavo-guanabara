# Desafio 019
# crie uma classe Livro, que vai simular a passagem de páginas de um livro,
# considerando também se o usuário chegou ao fim da leitura.


class Livro:
    def __init__(self, titulo, total_pags):
        self.titulo = titulo
        self.total_pags = total_pags
        self.pagina_atual = 0

    def avancar_paginas(self, n_pags=1):
        self.pagina_atual = self.pagina_atual + n_pags

        if self.pagina_atual < self.total_pags:
            return print(f"Você está na página {self.pagina_atual}")

        else:
            self.pagina_atual = self.total_pags
            print(f"Você está na página {self.pagina_atual}")
            print(f"Você chegou ao final do livro '{self.titulo}'!' Parabéns!")

        return


l1 = Livro("Game of Thrones", 100)
l1.avancar_paginas(2)
l1.avancar_paginas(3)
l1.avancar_paginas(1)
l1.avancar_paginas(1)
l1.avancar_paginas(1)
l1.avancar_paginas(65465465)
l1.avancar_paginas(35)
l1.avancar_paginas(42)
l1.avancar_paginas(1)
l1.avancar_paginas(1)
l1.avancar_paginas(1)
