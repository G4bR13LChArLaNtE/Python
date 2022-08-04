r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))

if (r1< (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < ( r1 + r2)):
	if r1 == r2 == r3:
		triangulo = "Equilátero"
	elif (r1 == r2) and (r1 != r3) or (r1 != r2) and (r1 == r3) or (r2 == r3) and (r2 != r1) or (r2 != r3) and (r3 == r1):
		triangulo = "Isósceles"
	elif r1 != r2 != r3:
		triangulo = "Escaleno"
	print("As retas {}, {} e {} podem ser um triângulo {}. ".format(r1,r2,r3, triangulo))
else:
	print("As retas {}, {} e {} não podem ser um triângulo. ".format(r1,r2,r3))