#Exercício 40:

'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2

print("Tirando a média entre {:.1f} e {:.1f} teremos {:.1f}".format(n1,n2,media))

if media < 5.0:
    print("Você foi reprovado, tente outra vez!")
elif (media >= 5.0) and (media <= 6.9):
    print("Você está de recuperação, estude para a prova e tudo vai dar certo!")
else:
    print("Parabéns você pasou!!!!!!!!! ;)")

print("Tenha ótimos estudos!")