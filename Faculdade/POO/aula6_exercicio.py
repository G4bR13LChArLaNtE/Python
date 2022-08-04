'''Exercício 01

Nome da classe
Carro
Atributos:
marca
modelo
placa
Métodos:
__init__(self, marca, modelo, placa)
exibir_dados(self)
Deve exibir os valores dos atributos do carro.

No programa principal, crie dois objetos da classe Carro, e
utilize o método exibir_dados para exibir os valores dos
atributos do carro no terminal.
'''


class Carro:

    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_dados(self):
        print(self.marca)
        print(self.modelo)
        print(self.placa)
        print()


carro1 = Carro('Ferrari', 'F50', 'FER-5050',)
carro2 = Carro('Lamborgini', 'Gallardo', 'LAM-2725',)
carro1.exibir_dados()
carro2.exibir_dados()


'''Exercício 02

Nome da classe
Funcionario
Atributos:
nome
sobrenome
salario_mensal
Métodos:
__init__(self, nome, sobrenome, salario_mensal)
O construtor deve fazer uma validação do salario_mensal,
e se o salário mensal não for positivo, deve configurá-lo como zero.
aumentar_salario(self)
Aumenta o salario do funcionário em 10%
salario_anual(self)
Deve retornar o salário anual do funcionário (soma dos salários mensais)

No programa principal, crie duas instâncias da classe Funcionario
e exiba o salário anual de cada funcionário (soma dos salários mensais).
Então dê a cada funcionário um aumento de 10% e exiba novamente o
salário anual de cada funcionário.
'''


class Funcionario:

    def __init__(self, nome, sobrenome, salario_mensal):
        self.nome = nome
        self.sobrenome = sobrenome
        if salario_mensal < 0:
            print("Valor incorreto!!! ")
            self.salario_mensal = 0
        else:
            self.salario_mensal = salario_mensal

    def aumentar_salario(self):
        self.salario_mensal = self.salario_mensal * 1.10

    def salario_anual(self):
        return (self.salario_mensal * 12)


funcionario1 = Funcionario('João', 'Silva', 2000.00)

funcionario1.aumentar_salario()
funcionario1.aumentar_salario()
funcionario1.aumentar_salario()

print(f'Nome: {funcionario1.nome},')
print(f'salário mensal: {funcionario1.salario_mensal},')
print(f'salário anual: {funcionario1.salario_anual()}.')


'''Exercício 03

Nome da classe:
ContaBancaria
Atributos:
numero
titular
senha
saldo (deve ser inicializado no construtor com o valor zero)
Métodos:
__init__(self, numero, titular, senha)
depositar(self, valor, senha)
Deve verificar se a senha informada está correta. Se estiver,
realiza a operação de depósito. Caso contrário,
deve exibir mensagem de “senha incorreta”.
sacar(self, valor, senha)
Deve verificar se a senha informada está correta. Se estiver,
realiza a operação de saque. Caso contrário,
deve exibir mensagem de “senha incorreta”.

No programa principal, crie uma conta bancária,
e realize operações de depósito e saque,
utilizando os métodos implementados na classe.
'''


class ContaBancaria:
    def __init__(self, numero, titular, senha, saldo):
        self.numero = numero
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        saldo = 0

    def depositar(self, valor, senha):
        if self.senha == senha:
            self.saldo += valor
        else:
            print("Senha incorreta")

    def sacar(self, valor, senha):
        if self.senha == senha:
            self.saldo -= valor
        else:
            print("Senha incorreta")


conta1 = ContaBancaria(123, "João da Silva", '6543', 2400.45)
conta2 = ContaBancaria(456, "Maria Mendes", '8765', 3655.99)

senha1 = input("Por favor, informe a senha!")
valor1_1 = float(input("Digite o valor: "))

conta1.depositar(valor1_1, senha1)

print(conta1.saldo)

senha2 = input("Por favor, informe a senha!")
valor2_2 = float(input("Digite o valor: "))

conta2.depositar(valor2_2, senha2)

print(conta2.saldo)


'''Exercício 04

Nome da classe
Aluno
Atributos:
ra
nome
turma
notas (lista que deve ser inicializada no construtor como vazia)
Métodos:
__init__(self, ra, nome, turma)
inserir_nota(self, nota)
Insere uma nota na lista de notas do aluno

No programa principal, crie 3 objetos da classe aluno.
Insira algumas notas para cada aluno.
Insira os objetos em uma lista.
Percorra a lista, calcule e exiba a média aritmética de cada aluno.
'''


class Aluno:

    def __init__(self, ra, nome, turma):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = []

    def inserir_nota(self, nota):
        self.notas.append(nota)


aluno1 = Aluno('202101', 'João da Silva', 'SI-2')
aluno2 = Aluno('202102', 'Maria da Silva', 'SI-1')
aluno3 = Aluno('202103', 'Thiago de Paula', 'SI-3')


alunos = [aluno1, aluno2, aluno3]

aluno1.inserir_nota(10)
aluno1.inserir_nota(8)
aluno1.inserir_nota(9)
aluno1.inserir_nota(7)

aluno2.inserir_nota(7)
aluno2.inserir_nota(6)
aluno2.inserir_nota(8)

aluno3.inserir_nota(9)
aluno3.inserir_nota(7)

for i in alunos:
    media = sum(i.notas) / len(i.notas)
    print('Nome: {} - Média: {}'.format(i.nome, media))
