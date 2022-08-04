'''Exercício 04

Implemente as classes de modo que obedeçam
os relacionamentos apresentados no diagrama abaixo.
O método acelerar da classe Veiculo deve
somar o valor passado por parâmetro à velocidade do veículo.
O método frear da classe Veiculo deve
subtrair o valor passado por parâmetro da velocidade do veículo.
O método imprimir_informacoes das classes Carro,
Moto e Bicicleta deve exibir na tela
o valor de cada um dos atributos da classe
(inclusive os atributos herdados da classe mãe)



Utilize o programa abaixo para testar as classes
carro = Carro("Ford", "Ka", 4, 85.0, 5)
moto = Moto("Honda", "Biz", 2, 9.2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

carro.imprimir_informacoes()
# imprime os valores de todos os atributos do carro
bike.imprimir_informacoes()
# imprime os valores de todos os atributos da bicicleta
moto.imprimir_informacoes()
# imprime os valores de todos os atributos da moto

# testar a velocidade atual
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15

'''


class Veiculo:
    def __init__(self, marca, modelo, rodas):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = 0

    def get_velocidade(self):
        return self.__velocidade

    def acelerar(self, valor):
        self.__velocidade += valor

    def frear(self, valor):
        self.__velocidade -= valor


class Automovel(Veiculo):
    def __init__(self, marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, rodas, marchas, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.marchas = marchas
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        print(self.marca)
        print(self.modelo)
        print(self.rodas)
        print(self.marchas)
        print(self.bagageiro)


class Carro(Automovel):
    def __init__(self, marca, modelo, rodas, potencia, portas):
        super().__init__(marca, modelo, rodas, potencia)
        self.portas = portas

    def imprimir_informacoes(self):
        print(self.marca)
        print(self.modelo)
        print(self.rodas)
        print(self.potencia)
        print(self.portas)


class Moto(Automovel):
    def __init__(self, marca, modelo, rodas, potencia, partidade_eletrica):
        super().__init__(marca, modelo, rodas, potencia)
        self.partidade_eletrica = partidade_eletrica

    def imprimir_informacoes(self):
        print(self.marca)
        print(self.modelo)
        print(self.rodas)
        print(self.potencia)
        print(self.partidade_eletrica)


carro = Carro("Ford", "Ka", 4, 85.0, 5)
moto = Moto("Honda", "Biz", 2, 9.2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

carro.imprimir_informacoes()
# imprime os valores de todos os atributos do carro
bike.imprimir_informacoes()
# imprime os valores de todos os atributos da bicicleta
moto.imprimir_informacoes()
# imprime os valores de todos os atributos da moto

# testar a velocidade atual
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15
