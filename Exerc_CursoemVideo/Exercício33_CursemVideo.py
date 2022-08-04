#Entrada de dados:
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

#Area do menor:
	
if n1 < n2 and n1 < n3:
	menor = n1

elif n3 < n1 and n3 < n2:
	menor = n3

else:
	menor = n2

	
#Area do maior:	

if n1 > n2 and n1 > n3:
	maior = n1
	
elif n2 > n1 and n2 > n3:
	maior = n2
	
else:
	maior = n3 
	
#Saída de dados:
	
print("\033[1;31;43mO número menor é o {}".format(menor))
print("\033[4;37;45mO número maior é o {}\033[m".format(maior))

