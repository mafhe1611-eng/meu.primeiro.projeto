import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    nome TEXT,
    altura REAL,
    idade INTEGER)
""")

# Inserir dados
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", ("\nJoão", 1.75, 20))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", ("\nMaria", 1.62, 25))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", ("\nAngela", 1.54, 19))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", ("\nRenato", 1.75, 29))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", ("\nDaniel", 1.73, 26))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", ("\nCarlos", 1.69, 30))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", ("\nJulia", 1.68, 22))


# Salvar mudanças
conexao.commit()

# Mostrar dados
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())

# Fechar conexão
conexao.close()
import sqlite3
