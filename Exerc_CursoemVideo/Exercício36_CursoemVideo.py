#Exercício 36

'''    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
       Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
       A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

cs = float(input("Qual o valor do imóvel? "))
sl = float(input("Qual o salário do comprador? "))
an = int(input("Em quantos anos ele vai pagar? "))
pr = cs/(an * 12)
print("Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f}.".format(cs, an, pr))


if pr <= (sl * 0.3):
    print("Seu emprestimo está aprovado! :) ")
else:
    print("Seu emprestimo foi negado infelizmente :(")

print("Tenha um bom dia!!!")

