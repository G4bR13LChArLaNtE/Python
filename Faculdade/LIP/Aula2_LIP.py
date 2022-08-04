#Aula 2 (Texto base aula 3)

n1 = float(input("Digite o número: "))
ep = float(input("Digite a exponencial: "))
n1 **= ep #equivalente  -> n1 = n1**ep

print("O valor é igual a {:.2f}.".format(n1))

n2 = float(input("Digite o número: "))
dv = float(input("Digite a divisão: "))
n3 = n2
n2 //= dv #equivalente -> n2 = n2//dv



print("A divisão inteira é igual a {:.2f}.".format(n2))

n3/=dv

print("A divisão é igual a {:.2f}.".format(n3))


a = 10
b = 10
c = 10

a*=2+3
b=b*2+3
c=c*(2+3)

print("Os valores são: ", a, b, c, )

a = 5
b = 4
c = 9
d = 7
e = 1
f = 2
s = 10
s += a + b ** (c-d) / e * f

print(s, end='') #end = '' serve para após imprimir o s pule para a próxima linha


'''
1.Escreva um algoritmo que leia duas variáveis inteiras e
troque o conteúdo entre elas.

2.Escreva um algoritmo que leia um número inteiro positivo e exiba o dobro desse número.

3.Escreva um algoritmo para calcular e exibir a média ponderada de 2 notas:
a.Nota1 (peso 6) b.Nota 2 (peso 4)

'''

# 1.Resposta:
a = int(input("Digite a variável A: "))
b = int(input("Digite a  variável B: "))

c = b
b = a
a = c

print("A é igual a:",a)
print("B é igual a:",b)

#2.Resposta:

a1 = int(input("Digite o número:"))
b = a1
b *= 2
print("O dobro do número é :", b)

#3.Resposta:

nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nt = ((nota1*0.6) + (nota2*0.4))
print("A média é igual a :", nt)