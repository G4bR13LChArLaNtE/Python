'''Exercício 2

Implementar um programa em Python que realize as seguintes operações:

Conectar com o banco de dados SQLITE e criar as tabelas
AUTOR e LIVRO (utilize os scripts abaixo para a criação das tabelas).
Criar as classes Autor e Livro e fazer o mapeamento das tabelas.
Inserir nas tabelas dois autores e dois livros.
Fazer uma consulta para verificar se os dados foram inseridos corretamente.

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")
'''

# Importar os módulos que serão utilizados
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE. Caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///aula14_exercicio2.db")
connection = engine.connect()

# Instancia da classe Base
Base = declarative_base(engine)

# Criação da sessão
session = Session()

# Exemplo de script para criar tabela no banco de dados SQLite
connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR(
           ID INTEGER PRIMARY KEY,
           NOME varchar(255) NOT NULL)""")

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO(
           ID INTEGER PRIMARY KEY,
           TITULO VARCHAR(255) NOT NULL,
           PAGINAS INT NOT NULL,
           AUTOR_ID INT NOT NULL)""")


# Mapeamento da tabela
class Autor(Base):
    __tablename__ = 'Autor'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable = False)

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = 'Livro'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable = False)
    paginas = Column('PAGINAS', Integer, nullable = False)
    autor_id = Column('AUTOR_ID', Integer, nullable = False)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


# Inserir dados (lista de objetos)
autor1 = Autor('Frank Herbert')
autor2 = Autor('J.R.R. Tolkien')
lista1 = [autor1, autor2]
session.add_all(lista1)
session.commit()        # NECESSÁRIO fazer o commit()

# Inserir dados (lista de objetos)
livro1 = Livro('Dune', 544, 1)
livro2 = Livro('The Lord of the rings', 468, 2)
lista2 = [livro1, livro2]
session.add_all(lista2)
session.commit()        # NECESSÁRIO fazer o commit()

# Busca todos os dados da tabela
print('-'*30)
result = session.query(Autor).all()           # retorna lista de objetos
for i in result:
    print(i.id, i.nome)

# Busca todos os dados da tabela
print('-'*30)
result = session.query(Livro).all()           # retorna lista de objetos
for i in result:
    print(i.id, i.titulo, i.paginas, i.autor_id)
