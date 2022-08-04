#Forma numérica:
n= int(input("Informe um número: "))
nu =((((n%100)*10)%100)//10)
nd = ((((n//10)%100)%10))
nc =((((n//100)%10)))
nm =(n//1000)
print("Unidades: {}".format(nu))
print("Dezenas: {}". format(nd))
print("Centenas: {}".format(nc))
print("Milhares: {}".format(nm))

#Forma string:
n = int(input('Informe um número: '))
num = str(n)
print('Unidades: {}'.format(num[3]))
print('Dezenas: {}'.format(num[2]))
print('Centenas: {}'.format(num[1]))
print('Milhares: {}'.format(num[0]))