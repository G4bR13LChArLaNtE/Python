'''Exercício 01 - Classe Livro
Implemente a classe Livro, conforme o diagrama a seguir.
No programa principal,
crie dois objetos da classe Livro.

Atributos:
titulo
autor
quantidade_paginas

Métodos:
Essa classe não possui métodos
'''


class Livro:
    def __init__(self, titulo, autor, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas


livro1 = Livro("Guerra e Paz", "Jorge Ping", 567)
livro2 = Livro("O bolo perfeito", "Dona Benta", 237)

print(livro1, livro2)

'''Exercício 02 - Classe Triangulo
Crie uma classe que representa um triângulo.

Atributos:
lado_a
lado_b
lado_c

Métodos:
calcular_perimetro: retorna o perímetro do triângulo (soma dos três lados).

Crie um programa que utilize esta classe. O programa deve
pedir ao usuário que informe as medidas dos três lados de
um triângulo. Depois deve criar um objeto com essas medidas
 e exibir seu perímetro.
'''


class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c


def calcular_perimetro(lado_a, lado_b, lado_c):
    perimetro = lado_a + lado_b + lado_c
    return perimetro


n1 = float(input("Digite o primeiro lado do triângulo, por favor: "))
n2 = float(input("Digite o segundo lado do triângulo, por favor: "))
n3 = float(input("Digite o terceiro lado do triângulo, por favor: "))
resultado = calcular_perimetro(n1, n2, n3)
print("O perímetro é igual a: ", resultado)


'''Exercício 03 - Classe Televisão
Implemente a classe Televisao.

Atributos:
canal (o canal inicial da tv deve ser None)
volume (o volume inicial da tv deve ser zero)

Métodos:
aumentar_volume: aumenta o nível de volume em uma unidade.
diminuir_volume: diminui o nível de volume em uma unidade.
alterar_canal: recebe o número do canal que será
sintonizado e altera o canal da tv.

Faça um programa para criar um objeto da classe Televisao
e testar a sua classe. Veja abaixo um trecho de programa que
utiliza a classe:

tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')        # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')        # A tv está no volume 2
'''


class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self, canal):
        self.canal = canal


tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')        # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')      # A tv está no volume 2


'''Exercício 04 - Classe Funcionário
Implemente uma classe Funcionario.

Atributos:
nome
salario

Métodos:
aumentar_salario: recebe como parâmetro de
entrada um percentual e altera o salário do funcionário,
de acordo com o percentual recebido.

Crie um programa que utilize esta classe.
Ele deve pedir ao usuário o nome e o salário do funcionário
 e criar um objeto da classe Funcionario. Depois, deve
 solicitar ao usuário o percentual de aumento e executar o
 método aumentar_salario. Na sequência deve imprimir o salário
'''


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        aumento = self.salario * percentual/100
        self.salario += aumento


nome = input("Nome do funcionario: ")
salario = float(input("Salário do funcionário: "))

funcionario1 = Funcionario(nome, salario)

percentual = float(input('Informe o percentual de aumento: '))
funcionario1.aumentar_salario(percentual)
print("{:.2f}".format(funcionario1.salario))

'''Exercício 05 - Classe Carro
Implemente uma classe Carro

Atributos:
quantidade_combustivel
(quantidade de litros de combustível no tanque do carro):
a  quantidade inicial deve ser zero.

Métodos:
adicionar_combustivel: recebe uma quantidade de
litros de combustível para abastecer o tanque.
obter_combustivel: retorna a quantidade atual de combustível.
andar: recebe uma distância em km e simula o
ato de dirigir o veículo por essa distância,
reduzindo o nível de combustível no tanque de gasolina.
Considere que o veiculo consome 0.20 litros de
combustivel por quilômetro percorrido.

Faça um programa para testar a classe Carro.
Veja abaixo um trecho de programa que utiliza a classe:

meu_carro = Carro()
meu_carro.adicionar_combustivel(20)                # Adiciona 20 litros
meu_carro.andar(80)                        # Andar 80 quilômetros
print('Litros de combustível no tanque:', meu_carro.obter_combustivel())

# deve imprimir: "Litros de combustível no tanque: 4.0"
'''


class Carro:

    def __init__(self):
        self.quantidade_combustivel = 0

    def adicionar_combustivel(self, quantidade):
        self.quantidade_combustivel += quantidade

    def obter_combustivel(self):
        return self.quantidade_combustivel

    def andar(self, distancia):
        consumo = distancia * 0.20
        self.quantidade_combustivel -= consumo


meu_carro = Carro()
meu_carro.adicionar_combustivel(20)
meu_carro.andar(80)
print(f"Litros de combustível no tanque: {meu_carro.obter_combustivel()}")
