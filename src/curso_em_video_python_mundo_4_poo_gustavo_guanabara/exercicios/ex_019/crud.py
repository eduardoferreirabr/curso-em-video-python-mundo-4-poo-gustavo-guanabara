import sqlite3
from pathlib import Path

# essa parte não tem no curso
# foi feita somente para resolver o problema do caminho do banco de dados
# Diretório onde está este arquivo Python
BASE_DIR = Path(__file__).resolve().parent

# Caminho do banco de dados
DB_PATH = BASE_DIR / "cadastro.db"

# # Verifica se o banco existe
# if not DB_PATH.exists():
#     raise FileNotFoundError(f"Banco não encontrado: {DB_PATH}")
# # -------------------------------------------------------------------------


def criar_banco() -> bool:

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pessoas (
                    cod INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    altura REAL NOT NULL
                );
            """)
        return True

    except sqlite3.Error as e:
        print(f"Falha na criação do banco: {e}")
        return False


def cadastrar_pessoa() -> bool:
    pass


def listar_pessoa() -> bool:
    pass


def atualizar_pessoa() -> bool:
    pass


def excluir_pessoa() -> bool:
    pass


def buscar_pessoa_por_nome() -> bool:
    pass
