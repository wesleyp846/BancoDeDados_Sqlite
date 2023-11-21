from sqlite4 import SQLite4

#Dando nome ao banco de dados
banco = SQLite4("teste.db")
#Iniciando o banco de dados
banco.connect()

#Criando uma tabela, NOme do banco de dados e nomedas colunas
banco.create_table("teste", ["coluna1", "coluna2"])
#Inserindo dados nas linhas do DB, relação chaves nomes
banco.insert("teste", {"coluna1": "Fabio", "coluna1": "João", "coluna2": "Joana"})

#acessando o DB
resultado = banco.select("teste")
print(resultado)

#Acessando o DB filtrando dados
resultado2 = banco.select("teste", columns=["coluna1"], condition='coluna1 = "Fabio"')
print(resultado2)
