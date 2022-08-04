def soma():
	soma1 = 0
	cont = 0
	for n in range (1,500,1):
		if n % 3 == 0 and not n % 2 == 0:
			soma1 +=  n
			cont += 1
	print("A soma dos números é igual a: ",soma1)
	return cont

	
soma1 = soma()	
print("E o total de números somados é igual a: ",soma1)