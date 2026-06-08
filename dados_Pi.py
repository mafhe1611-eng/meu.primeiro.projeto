import sqlite3

conexao = sqlite3.connect("banco_Pi.db")

cursor = conexao.cursor()

# Criar tabela
cursor.execute(""";
CREATE TABLE IF NOT EXISTS pessoas (
    Nome TEXT,
    Idade INTEGER,
    Genero TEXT,
    Tipo de Machucado TEXT,
    Gravidade do Machucado TEXT            )
""")

# Inserir dados
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Carlos Silva",34,'Masculino','Fratura Fechada (Braço)','Moderada'))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Mariana Costa",22,'Feminino','Corte profundo (Mão)','Moderada'))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Roberto Souza",45,'Masculino','Contusão torácica','Grave' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Ana Júlia Lima",8,'Feminino','Escoreação (Joelho)','Leve' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Ricardo Oliveira",61,'Masculino','Entorse de tornozelo','Leve' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Beatriz Santos",29,'Feminino','Queimadura','Grave' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Fernando Almeida",73,'Masculino','Traumatismo Craniano leve','Critica' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Camila Ribeiro",19,'Feminino','Picada de inseto com alergia','Moderada' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Lucas Martins",41,'Masculino','Lacerção no pé','Moderada' ))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Juliana Rocha", 55, "Feminino", "Luxação de ombro", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Bruna Sousa", 24, "Feminino", "Torção do tornozelo", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("João Santos", 4, "Masculino", "Fratura no braço", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Pedro Costa", 42, "Masculino", "Queimadura de 2º grau", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Carla Souza", 28, "Feminino", "Torção no tornozelo", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Lucas Ferreira", 31, "Masculino", "Corte profundo na perna", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Juliana Lima", 22, "Feminino", "Hematoma no braço", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Rafael Gomes", 45, "Masculino", "Fratura na perna", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Fernanda Alves", 37, "Feminino", "Queimadura leve", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Bruno Rocha", 26, "Masculino", "Luxação no ombro", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Camila Martins", 30, "Feminino", "Corte no pé", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Gabriel Pereira", 21, "Masculino", "Escoriações múltiplas", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Patrícia Ribeiro", 39, "Feminino", "Fratura no pulso", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Felipe Carvalho", 27, "Masculino", "Torção no joelho", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Larissa Melo", 24, "Feminino", "Corte superficial", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Thiago Barbosa", 36, "Masculino", "Queimadura química", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Renata Castro", 33, "Feminino", "Contusão nas costas", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("André Nunes", 29, "Masculino", "Fratura na clavícula", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Beatriz Araújo", 18, "Feminino", "Arranhão no braço", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Marcelo Teixeira", 50, "Masculino", "Corte profundo no antebraço", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Daniela Freitas", 27, "Feminino", "Torção no punho", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Eduardo Lopes", 32, "Masculino", "Hematoma na perna", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Vanessa Cardoso", 41, "Feminino", "Fratura no tornozelo", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Ricardo Mendes", 23, "Masculino", "Escoriação no rosto", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Aline Rodrigues", 35, "Feminino", "Queimadura solar", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Gustavo Fernandes", 38, "Masculino", "Luxação no cotovelo", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Natália Pinto", 20, "Feminino", "Corte no dedo", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Diego Moreira", 44, "Masculino", "Fratura nas costelas", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Priscila Dias", 31, "Feminino", "Contusão no ombro", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Vinícius Cunha", 28, "Masculino", "Corte na testa", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Tatiane Moura", 26, "Feminino", "Arranhões múltiplos", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Leonardo Ramos", 40, "Masculino", "Queimadura de 3º grau", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Sabrina Vieira", 29, "Feminino", "Torção no pé", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Mônica Farias", 46, "Feminino", "Fratura no dedo", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Paulo Rezende", 52, "Masculino", "Corte profundo na mão", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Letícia Guimarães", 23, "Feminino", "Escoriação no joelho", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Henrique Azevedo", 35, "Masculino", "Luxação no joelho", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Isabela Duarte", 32, "Feminino", "Contusão abdominal", "Moderada"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Alexandre Machado", 48, "Masculino", "Fratura no fêmur", "Grave"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Maria Oliveira", 17, "Feminino", "Arranhão no joelho", "Leve"))
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?, ?, ?)", ("Rodrigo Batista", 24, "Masculino", "Hematoma facial", "Moderada"))

# Salvar mudanças
conexao.commit()

# Mostrar dados
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())

# Fechar conexão
conexao.close()