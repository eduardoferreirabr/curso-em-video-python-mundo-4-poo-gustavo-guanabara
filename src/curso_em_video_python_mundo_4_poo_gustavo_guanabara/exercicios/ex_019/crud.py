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


def cadastro_em_massa():
    cad_pessoas = [
        ("1", "Gustavo", "1.84"),
        ("2", "Gabriela", "1.63"),
        ("3", "Pedro", "2.02"),
        ("4", "Mariana", "1.72"),
    ]

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                """
                INSERT OR IGNORE INTO pessoas (cod, nome, altura) VALUES (?, ?, ?)
            """,
                cad_pessoas,
            )

    except sqlite3.Error as e:
        print(f"[ERRO] Falha ao fazer cadastro em massa: {e}")


def cadastrar_pessoa() -> bool:
    print("\n === NOVO CADASTRO DE PESSOA ===")

    # Leitura e validação dos dados
    val_nome = input("Nome: ").strip()
    if not val_nome:
        print("[ERRO] O nome é um campo obrigatório.")
        return False

    val_altura = input("Altura (metros): ").strip().replace(",", ".")
    if not val_altura:
        print("[ERRO] A altura é um campo obrigatório.")
        return False

    try:
        altura = float(val_altura)
        if altura <= 0.30 or altura > 3.0:
            print("[ERRO] Valor incoerente para altura!.")
            return False
    except ValueError:
        print("[ERRO] A altura precisa ser um número.")
        return False

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO pessoas (nome, altura) VALUES (?, ?)",
                (val_nome, altura),
            )
            print(f"Cadastro de {val_nome} realizado com sucesso")
            return True

    except sqlite3.Error as e:
        print(f"[ERRO] Falha no cadastro do banco: {e}")
        return False


def listar_pessoa() -> bool:
    pass


def atualizar_pessoa() -> bool:
    pass


def excluir_pessoa() -> bool:
    pass


def buscar_pessoa_por_nome() -> bool:
    pass
