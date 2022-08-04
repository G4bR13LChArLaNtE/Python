#Exercício 39:

'''
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
 Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = (ano_atual - ano_nasc)

if idade < 17:
    print("Ainda não é o tempo de você se alistar.")

elif (idade > 17) and (idade <= 18):
    print("Está na hora exata de você se alistar, procure a junta militar mais próxima da sua casa.")

elif idade > 18:
    print("Já se passou o tempo certo para você se alistar")

print("Tenha um bom dia! :)")

#Resolução Curso em Video:

atual = datetime.date.today().year
nasc = int(input("Digite o ano de nascimento: "))
idade2 = atual - nasc
print("Quem nasceu em {} tem {} anos em {}".format(nasc,idade2,atual))
if idade2 == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade2 < 18:
    print("Ainda faltam {} anos para o alistamento.".format(18 - idade2))
elif idade2 > 18:
    print("Você já deveria ter se alistado há {} anos".format(idade - 18))

print("Tenha um bom dia! :)")