'''Exercício 1

Implementar um programa em Python que realize as seguintes operações:

Conectar com o banco de dados SQLITE e criar a tabela FUNCIONARIO (utilize o
script abaixo para a criação da tabela).
Criar uma classe Funcionario e mapear a tabela criada anteriormente.
Instanciar três objetos da classe Funcionario.
Inserir os dados dos objetos na tabela.
Realizar uma consulta na tabela de funcionários e
verificar se os dados foram inseridos corretamente.
Realizar uma consulta na tabela de todos os funcionários
com salário superior a R$ 1.500,00.

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""") '''

# Importar os módulos que serão utilizados
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE. Caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///aula14_exercicio1.db")
connection = engine.connect()

# Instancia da classe Base
Base = declarative_base(engine)

# Criação da sessão
session = Session()

# Exemplo de script para criar tabela no banco de dados SQLite
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO(
                      ID INTEGER PRIMARY KEY,
                      NOME VARCHAR(255) NOT NULL,
                      IDADE INT NOT NULL,
                      SALARIO FLOAT NOT NULL)""")


# Mapeamento da tabela
class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable = False)
    idade = Column('IDADE', Integer, nullable = False)
    salario = Column('SALARIO', Float, nullable = False)

    def __init__(self, nome, idade, salario):        # Construtor
        self.nome = nome
        self.idade = idade
        self.salario = salario

# Inserir dados (um objeto)
func = Funcionario('Jorge', 27, 1879)            # criar o objeto
session.add(func)
session.commit()                                # necessario fazer o commit()

# Inserir dados (lista de objetos)
func1 = Funcionario('João', 32, 1450)
func2 = Funcionario('Lucas', 29, 2200)
lista = [func1, func2]
session.add_all(lista)
session.commit()        # NECESSÁRIO fazer o commit()

# Busca todos os dados da tabela
print('-'*30)
result = session.query(Funcionario).all()           # retorna lista de objetos
for i in result:
    print(i.id, i.nome, i.idade, i.salario)

# Busca utilizando filtros
# salario maior que 1500 (.all() para retornar todos)
print('-'*30)
d = session.query(Funcionario).filter(Funcionario.salario>1500).order_by(Funcionario.nome).all()
for i in d:
    print(i.id, i.nome, i.idade, i.salario)
