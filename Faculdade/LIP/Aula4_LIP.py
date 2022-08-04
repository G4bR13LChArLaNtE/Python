'''Crie um programa que solicite ao usuário um número de 1 à 7 e exiba o dia da
semana correspondente. Assuma que a semana começa no domingo (1) e termina no
sábado (7). Use apenas seleção simples, ou seja, sem else nem elif.
2) Refaça o exercício anterior, agora utilizando a seleção encadeada, mas sem usar o
comando elif, de modo que seja observada a importância do alinhamento correto de
indentação entre os diversos comandos if e else.
3) Refaça o exercício anterior, agora utilizando elif.
4) Com o Python Tutor, compare o fluxo de execução dos códigos dos exercícios
anteriores.'''

#Resposta exercício 2:

n1 = int(input("Digite um número de 1 a 7 para os dias da semana: "))
if n1 == 1:
    print("Hoje é Domingo!")
else:
    if n1 == 2:
        print("Hoje é segunda!")
    else:
        if n1 == 3:
           print("Hoje é terça!")
        else:
            if n1 == 4:
                print("Hoje é quarta!")
            else:
                if n1 == 5:
                    print("Hoje é quinta!")
                else:
                    if n1 == 6:
                        print("Hoje é sexta!")
                    else:
                        if n1 == 7:
                            print("Hoje é sábado!")
print("Tenha um bom dia!")

