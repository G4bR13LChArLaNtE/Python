'''Exercício 01

O diagrama abaixo fornece uma hierarquia de
classes onde a classe Pessoa é a superclasse
(classe mãe), e as classes PessoaFisica e
PessoaJuridica são as subclasses (classes filhas).
Crie a classe Pessoa com os atributos identificador
e nome.
Crie a classe PessoaJuridica que herda da classe
Pessoa e acrescenta o atributo cnpj.
Crie a classe PessoaFisica que herda da classe Pessoa
e acrescenta os atributos rg e cpf.'''


class Pessoa:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome


class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome, cnpj):
        super().__init__(identificador, nome)
        self.cnpj = cnpj


class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome, rg, cpf):
        super().__init__(identificador, nome)
        self.rg = rg
        self.cpf = cpf


pessoa1 = Pessoa(1, "Nome da Pessoa")
p_juridica = PessoaJuridica(2, "Nome da Pessoa Juridica", "1111111111")
p_fisica = PessoaFisica(3, "Nome da Pessoa Fisica", "222222222", "333333333")

print(pessoa1.identificador)        # 1
print(pessoa1.nome)                 # Nome da Pessoa

print(p_juridica.identificador)     # 2
print(p_juridica.nome)              # Nome da Pessoa Juridica
print(p_juridica.cnpj)              # 1111111111

print(p_fisica.identificador)       # 3
print(p_fisica.nome)                # Nome da Pessoa Fisica
print(p_fisica.rg)                  # 222222222
print(p_fisica.cpf)                 # 333333333
