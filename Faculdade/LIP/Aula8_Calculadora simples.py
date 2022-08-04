'''
Calculadora simples:

1° menu()
2° entrada_de_dados()
3° adicao()
4° subtracao()
5° multiplicador()
6° divisao()
7° imprimir()
8° controlador()
'''

#Função Menu:

def menu():
    print("..Menu..")
    print(" Digite os seguintes números para acessar as opções: ")
    print()
    print(" 1 - Adição ")
    print(" 2 - Subtração ")
    print(" 3 - Multiplicação ")
    print(" 4 - Divisão ")
    print()

    op = int(input("Digite por favor a opção a sua escolha: "))
    print()

    return op

#Função entrada de dados:

def entradas_de_dados():
    print("..Entrada de dados..")
    n = float(input("Digite o número: "))
    print()

    return n



#Função adição:

def adicao(n1,n2):
    print("..Adição..")
    soma = n1 + n2
    print()

    return soma

#Função subtração:

def subtracao(n1,n2):
    print("..Subtração..")
    sub = n1 - n2
    print()

    return sub

#Função Multiplicação:

def multiplicador(n1,n2):
    print("..Multiplicação..")
    mult = n1 * n2
    print()

    return mult

#Função Divisão:

def divisao(n1,n2):
    print("..Divisão..")
    div = n1 / n2
    print()

    return div

#Função imprimir:

def imprime(result):
    print("..Imprimir..")
    print(" O resultado da sua operação é igual a {:.2f}.".format(result))
    print()

    return 0



#Função controladora:

def controlador(n1,n2,op):
    print("..Controlador..")
    if(op == 1):
        result = adicao(n1,n2)
    elif(op == 2):
        result = subtracao(n1,n2)
    elif(op == 3):
        result = multiplicador(n1, n2)
    elif(op == 4):
        result = divisao(n1,n2)

    return result

#Função principal:

print("..Principal..")

print()
print()

op = menu()
n1 = entradas_de_dados()
n2 = entradas_de_dados()

result = controlador(n1, n2, op)

imprime(result)



