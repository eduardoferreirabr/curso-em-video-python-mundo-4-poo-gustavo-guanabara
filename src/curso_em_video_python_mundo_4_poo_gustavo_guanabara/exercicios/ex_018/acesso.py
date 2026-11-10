import sqlite3
from pathlib import Path

# essa parte não tem no curso
# foi feita somente para resolver o problema do caminho do banco de dados
# Diretório onde está este arquivo Python
BASE_DIR = Path(__file__).resolve().parent

# Caminho do banco de dados
DB_PATH = BASE_DIR / "meubanco.db"

# Verifica se o banco existe
if not DB_PATH.exists():
    raise FileNotFoundError(f"Banco não encontrado: {DB_PATH}")
# -------------------------------------------------------------------------

# Estabelece a conexão
# conn = sqlite3.connect(DB_PATH)

busca = input("Quem você está procurando? ").strip()
try:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row  # Permite acessar os dados por nome de coluna

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM amigos WHERE nome LIKE ?", (f"%{busca}%",))

        # lista = cursor.fetchall()
        # print(lista)

        # for amigo in cursor:
        #     print(amigo)

        # for amigo in cursor:
        #     print(f"{amigo[1]} nasceu em {amigo[2]}.")

        total = 0

        for total, amigo in enumerate(cursor, start=1):
            print(f"{amigo['nome']} nasceu em {amigo['nascimento']}.")

        print(f"Ao todo encontrei {total} amigos com '{busca}'.")

except sqlite3.Error as e:
    print(f"Erro ao acessar o banco de dados: {e}")

except Exception as e:
    print(f"Algo deu errado: {e}")

# cursor.close()
# conn.close()

print("ACABOU!")
