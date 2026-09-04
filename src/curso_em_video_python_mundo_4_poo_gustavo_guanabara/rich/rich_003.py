from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="right", style="red")
tabela.add_column("Preço", justify="center", style="blue")

tabela.add_row("Lápis", "R$ 1,50")
tabela.add_row("Borracha", "[green]R$ 5,00[/]")

print(tabela)
