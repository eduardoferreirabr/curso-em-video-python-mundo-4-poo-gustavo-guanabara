import sqlite3
from pathlib import Path

# Diretório onde está este arquivo Python
BASE_DIR = Path(__file__).resolve().parent

# Caminho do banco de dados
DB_PATH = BASE_DIR / "meubanco.db"

# Verifica se o banco existe
if not DB_PATH.exists():
    raise FileNotFoundError(f"Banco não encontrado: {DB_PATH}")

# Estabelece a conexão
conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()
cursor.execute("SELECT * FROM amigos")

lista = cursor.fetchall()

print(lista)

cursor.close()
conn.close()
