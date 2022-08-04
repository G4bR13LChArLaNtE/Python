'''Exercício 1
Crie as tabelas abaixo no banco de dados SQLITE e
faça o mapeamento dessas tabelas utilizando o SQLAlchemy.
Implementar um programa para realizar as seguintes operações:
Cadastrar um médico.
Cadastrar dois pacientes.
Cadastrar dois exames (um para cada paciente).
Inserir os dados cadastrados banco de dados.
Realizar uma consulta no banco de dados para verificar
se os dados foram inseridos corretamente.

Scripts para criação das tabelas no banco de dados:
connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")

connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")

connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")

'''
# Importar os módulos que serão utilizados
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql.sqltypes import VARCHAR

# Criar Conexão com Banco SQLITE. Caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///aula15_exercicio1.db")
connection = engine.connect()

# Instancia da classe Base
Base = declarative_base(engine)

# Criação da sessão
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS PACIENTE (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CPF VARCHAR(255),
                        IDADE INTEGER)""")


# Mapeamento da Tabela Paciente:
class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String(255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):   # Construtor:
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


connection.execute("""CREATE TABLE IF NOT EXISTS MEDICO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        CRM VARCHAR(255),
                        ESPECIALIZACAO VARCHAR(255))""")


# Mapeamento da Tabela Medico:
class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', String(255))
    especializacao = Column('ESPECIALIZACAO', Integer)

    def __init__(self, nome, crm, especializacao):        # Construtor
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


connection.execute("""CREATE TABLE IF NOT EXISTS EXAME (
                        ID INTEGER PRIMARY KEY,
                        ID_MEDICO INTEGER,
                        ID_PACIENTE INTEGER,
                        DESCRICAO VARCHAR(255),
                        RESULTADO VARCHAR(255))""")


# Mapeamento da Tabela Exame:
class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID_MEDICO', Integer)
    id_paciente = Column('ID_PACIENTE', Integer)
    descricao = Column('DESCRICAO', String(255))
    resultado = Column('RESULTADO', String(255))

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado


# Inserirndo os dados (objeto) da Tabela Medico:
med1 = Medico('Douglas', '20256', 'Cardiologia')            # criar o objeto
session.add(med1)
session.commit()                                # necessario fazer o commit()

# Inserir dados (lista de objetos) da Tabela Paciente:
pac1 = Paciente('Jefferson', '23547890111', 27)
pac2 = Paciente('Thiago', '13476278933', 34)
paci = [pac1, pac2]
session.add_all(paci)
session.commit()                                # necessario fazer o commit()

# Inserir dados (lista de objetos) da Tabela Exame:
exa1 = Exame(1, 2, 'Eletrocardiograma', 'Tudo nos conformes.')
exa2 = Exame(1, 1, 'Ecocardiograma', 'Notou-se uma alteração.')
exames = [exa1, exa2]
session.add_all(exames)
session.commit()                                # necessario fazer o commit()


# Busca todos os dados da tabela Paciente
print('-'*30)
result = session.query(Paciente).all()
# retorna lista de objetos
for i in result:
    print(i.id, i.nome, i.cpf, i.idade)

print()
print()

# Busca todos os dados da tabela Medico
print('-'*30)
result = session.query(Medico).all()
# retorna lista de objetos
for i in result:
    print(i.id, i.nome, i.crm, i.especializacao)

print()
print()

# Busca todos os dados da tabela Medico
print('-'*30)
result = session.query(Exame).all()
# retorna lista de objetos
for i in result:
    print(i.id, i.id_medico, i.id_paciente, i.descricao, i.resultado)

# retornando objetos de mais de uma Tabela:
resultado = session.query(Medico, Paciente, Exame).filter(
    Exame.id_paciente == Paciente.id, Exame.id_medico == Medico.id)
for obj in resultado:
    print(obj.Medico.nome, obj.Paciente.nome, obj.Exame.descricao,
          obj.Exame.resultado)

# Fechar conexão com o Banco de Dados:
connection.close()
