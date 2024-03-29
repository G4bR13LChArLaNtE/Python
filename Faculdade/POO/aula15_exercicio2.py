'''Crie a tabela abaixo no banco de dados SQLITE
e faça o mapeamento dessa tabela utilizando o SQLAlchemy.
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")

Considere um arquivo de texto contendo os dados
dos funcionários de uma empresa.
Cada linha do arquivo contém as informações
sobre um funcionário (separados por ponto-e-virgula).
Implementar um programa para realizar as seguintes operações:
Abrir e ler o conteúdo do arquivo de texto.
Inserir os dados na tabela do banco de dados.
Realizar uma consulta no banco de dados para
verificar se os dados foram inseridos corretamente.

Exemplo de arquivo de texto com os dados dos funcionários:
Eugenio Saloio;24;3005.99
Zelvio Caeira;38;1947.42
Eusebio Maior;28;4686.53
Evaristo Lemos;42;3313.16
Fabiana Barros;24;4172.35
Alcides Freire;34;3623.39
Alda Madureira;27;1615.73
Alexandra Pardo;52;2529.51
Antonio Tupinamba;28;3778.39
Aurora Landim;33;4029.46
Balduino Baldaia;43;1956.86
Belmiro Brion;27;1394.02
Bruno Figueira;61;1287.75
Catarina Vega;53;2697.87
Cecilia Franca;43;1829.95
Claudemira Leme;63;2660.89
Constanca Bulhoes;23;2854.26
Abel Lagos;29;4770.14
Adelaide Montero;22;2818.96
Aires Batata;70;4474.44
Fabiano Castelhano;44;4357.99
Fabiola Puentes;51;1633.88
Felicia Mieiro;58;1547.87
Ferdinando Rosario;19;1242.27
Frederica Aguiar;70;2189.78
Fatima Valle;54;1092.64
Gil Cesario;60;4544.78
Gina Simao;64;4992.36
Godim Jatoba;23;1209.92
Godo Coello;59;2858.88
Goncalo Quental;26;2513.53
Jurema Madeira;23;2475.49
Justino Cezimbra;53;1040.82
Jessica Veloso;37;2484.33
Mamede Cipriano;22;3363.51
Marco Braz;40;1345.21
Maximiliano Veleda;59;1384.40
Salvador Padilla;21;3488.65
Sidonio Sales;51;2196.13
Teresa Freyria;40;4718.89
Jonatas Nazario;49;2006.47
Leonilde Gentil;66;1312.00
Leonir Fuentes;50;3478.60
Levindo Cerqueira;47;4149.13
Liedson Pardo;65;3259.65
Lourenco Suarez;69;3019.36
Lucilia Lousa;53;3757.28
Tomas Vidal;40;2228.28
Xico Azevedo;41;4795.57
Giovana Caetano;34;3971.72

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

connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")


# Mapeamento da Tabela Funcionario:
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


# Ler arquivo de texto:
# o arquivo já deve existir
# procura no diretório do programa
arquivo = open("aula15_exercicio2.txt", "r", encoding="UTF-8")      # r = read

funcionarios = []

for linha in arquivo:   # percorre o arquivo
    lista = linha.split(';')
    func1 = Funcionario(lista[0], int(lista[1]), float(lista[2]))
    funcionarios.append(func1)

session.add_all(funcionarios)
session.commit()                                # necessario fazer o commit()

# Busca todos os dados da tabela Paciente
print('-'*30)
result = session.query(Funcionario).all()
# retorna lista de objetos
for i in result:
    print(i.id, i.nome, i.idade, i.salario)

print()
print()

arquivo.close()
connection.close()
