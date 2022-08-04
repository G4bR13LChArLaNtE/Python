#URI - 1165 - Doação:

n1 = float(input())
soma = 0
while True:
	if n1 == -1:
		break
	n1 = float(n1)
	soma += n1
	n1 = float(input())
print(soma)