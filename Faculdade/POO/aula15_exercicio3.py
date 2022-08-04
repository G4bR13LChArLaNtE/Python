'''Exercício 3
Faça um programa que copie os dados da tabela de
funcionários do banco de dados (inseridos no exercício anterior)
e salve esses dados em um novo arquivo de texto.

Nesse novo arquivo, a listagem dos funcionarios deve
ser feita em ordem alfabética.
'''

# Importar os módulos que serão utilizados
import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


# Criar Conexão com Banco SQLITE. Caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///aula15_exercicio2.db")
connection = engine.connect()

# Instancia da classe Base
Base = declarative_base(engine)

# Criação da sessão
session = Session()


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)

    def __init__(self, nome, idade, salario):        # Construtor
        self.nome = nome
        self.idade = idade
        self.salario = salario


# Criar um arquivo de texto:
arquivo = open('aula15_exercicio3.txt', 'w', encoding='utf-8')

# Realizar a consulta do banco de dados:
resultado = session.query(Funcionario).order_by(Funcionario.nome)
for obj in resultado:
    arquivo.write(obj.nome + ';' + str(obj.idade) +
                  ';' + str(obj.salario) + '\n')

arquivo.close()
connection.close()
