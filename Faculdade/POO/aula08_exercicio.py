'''Exercício 01

Altere a classe Funcionario do programa abaixo:
Transforme os seus atributos em atributos privados.
Crie os métodos get e set para todos os atributos.
Faça as demais alterações necessárias para que o
programa funcione corretamente.
'''

'''
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario


func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.set_salario(2000.0)                # Altera salário
print("Nome:", func1.get_nome())
print("CPF:", func1.get_cpf())
print("Salário:", func1.get_salario())
'''

'''Exercício 02

Implemente a classe Filme, conforme o diagrama de classes abaixo
Todos os atributos devem ser privados
Crie os métodos get e set para todos os atributos

No seu programa principal, faça a seguinte implementação:
Criar uma lista de filmes vazia
Cadastrar 3 filmes (com os dados informados pelo usuário)
Armazenar os dados de cada filme em um objeto da classe Filme
Armazenar os objetos na lista de filmes
Exibir um relatório com os dados de todos os filmes cadastrados

'''
'''

class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


filmes = []
for i in range(3):
    titulo = str(input("Digite o nome do filme: "))
    genero = str(input("Digite o genero desse filme: "))
    filme = Filme(titulo, genero)
    filmes.append(filme)

for filme in filmes:
    print()
    print("O Título do filme é: ", filme.get_titulo())
    print("O Genero desse filme é: ", filme.get_genero())
'''

'''Exercício 03

Implemente as classes ContaBancaria e Cliente, conforme o diagrama
de classes abaixo.



Classe Cliente
Atributos (todos definidos no construtor):
nome: nome do cliente (público)
cpf: cpf do cliente (privado)
senha: senha do cliente (privado)
Métodos:
get_senha: retorna a senha do cliente


Classe ContaBancaria
Atributos:
numero: numero da conta (público)
cliente: objeto Cliente associado à conta (público)
saldo: saldo da conta (privado). Deve começar sempre com zero.
Métodos:
get_saldo: retorna o saldo da conta.
depositar: recebe como parâmetros de entrada um valor e uma senha.
Acrescenta esse valor ao saldo da conta apenas se a senha for igual à senha do
cliente.
sacar: recebe como parâmetros de entrada um valor e uma senha.
Subtrai esse valor do saldo da conta, apenas se a senha for igual à senha do
cliente.

Utilize o código abaixo para testar as suas classes
cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime 150

'''


class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha


class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo += + valor
        else:
            print("Senha invalida")

    def sacar(self, valor, senha):
        if senha == self.cliente.get_senha():
            self.__saldo -= valor
        else:
            print("Senha invalida")


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime 150

'''Classe CarroCorrida

Atributos (todos privados):
numero: número de identificação do carro
piloto: nome do piloto do carro ao carro
velocidade_maxima: velocidade máxima do carro em km/h
velocidade_atual: velocidade atual do carro em km/h
(valor inicial deve ser zero)
ligado: informa se o carro está ligado (valor inicial deve ser False)


Métodos:
ligar: define o carro como ligado
desligar: define o carro como desligado
acelerar: aumenta velocidade atual do carro em N km/h. O carro só pode
acelerar se estiver ligado. Ao acelerar,
o carro nunca pode ultrapassar a sua velocidade máxima
frear: define a velocidade atual do carro em 0 km/h.
Criar os métodos get e set, quando for necessário. '''


class CarroCorrida:
    def __init__(self, numero, piloto, velocidade_maxima):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_maxima = velocidade_maxima
        self.__velocidade_atual = 0
        self.__ligado = False

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def acelerar(self, velocidade):
        if self.__ligado is True:
            self.__velocidade_atual += velocidade
            if self.__velocidade_maxima < self.__velocidade_atual:
                self.__velocidade_atual = self.__velocidade_maxima

    def frear(self):
        self.__velocidade_atual = 0

    def get_velocidade_atual(self):
        return self.__velocidade_atual


carro = CarroCorrida(1, "Paulo", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())
carro.ligar()
carro.acelerar(20)
print(carro.get_velocidade_atual())
carro.acelerar(80)
print(carro.get_velocidade_atual())
carro.acelerar(70)
print(carro.get_velocidade_atual())
carro.frear()
print(carro.get_velocidade_atual())
