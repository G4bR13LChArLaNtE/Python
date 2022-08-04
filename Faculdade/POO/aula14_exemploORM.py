# Importar os módulos que serão utilizados
import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE. Caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()

# Instancia da classe Base
Base = declarative_base(engine)

# Criação da sessão
session = Session()

# Exemplo de script para criar tabela no banco de dados SQLite
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)


# Mapeamento da tabela
class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):        # Construtor
        self.nome = nome
        self.idade = idade
        self.salario = salario


# Inserir dados (um objeto)
func = Funcionario('Zezinho', 20, 1700)            # criar o objeto
session.add(func)
session.commit()                                # necessario fazer o commit()

# Inserir dados (lista de objetos)
func1 = Funcionario('Luizinho', 22, 1250)
func2 = Funcionario('Huguinho', 22, 2000)
lista = [func1, func2]
session.add_all(lista)
session.commit()        # NECESSÁRIO fazer o commit()

# Busca todos os dados da tabela
print('-'*30)
result = session.query(Funcionario).all()
           # retorna lista de objetos
for i in result:
    print(i.id, i.nome, i.idade, i.salario)

# Busca um dado específico (pela primary key)
print('-'*30)
func = session.query(Funcionario).get(2)
          # busca pela chave primária e retorna o objeto
print(func.id, func.nome, func.idade, func.salario)

# Busca utilizando filtros
# salario maior que 1500 (.all() para retornar todos)
print('-'*30)
d = session.query(Funcionario).filter(Funcionario.salario>1500).order_by(Funcionario.nome).all()
for i in d:
    print(i.id, i.nome, i.idade, i.salario)

# Busca utilizando vários filtros (.all() para retornar todos)
print('-'*30)
d = session.query(Funcionario).filter(Funcionario.idade == 22, Funcionario.nome.like('%inho%')).all()
for i in d:
    print(i.id, i.nome, i.idade, i.salario)

# Busca utilizando filtros (.first() retorna apenas o primeiro)
print('-'*30)
d = session.query(Funcionario).filter(Funcionario.idade == 22, Funcionario.nome.like('%inho%')).first()
print(d.id, d.nome, d.idade, d.salario)

# Alterar um registro
func = session.query(Funcionario).get(1)        # busca um objeto
func.nome = 'Zezinho da Silva'                    # altera os atributos do objeto
func.idade = 25
session.commit()                        # realiza o commit

# Excluir um registro
func = session.query(Funcionario).get(2)        # busca um objeto
session.delete(func)                    # deleta o objeto
session.commit()

# Fechar conexão com banco de dados
connection.close()
