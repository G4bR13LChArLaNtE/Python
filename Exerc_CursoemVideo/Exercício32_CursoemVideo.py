ano = int(input("Qual ano sera analisado? "))
if (ano % 4 == 0 and ano % 100 != 0) or ano %400 == 0 :
	print("O ano de {} é bissexto. ".format(ano))
else:
	print("Esse ano ({}) não é bissexto. ".format(ano))