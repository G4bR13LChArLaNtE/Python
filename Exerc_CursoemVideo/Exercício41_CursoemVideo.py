ano = int(input("Digite o ano de nascimento do atleta: "))
data_atual = int(input("Digite o ano atual: "))
idade = data_atual - ano

if idade <= 9:
	print("O atleta pertence a cateforia MIRIM! ")
elif idade > 9 and idade <= 14:
	print("O atleta pertence a categoria INFANTIL! ")
elif idade > 14 and idade <= 19:
	print("O atleta pertence a categoria JÚNIOR! ")
elif idade > 19 and idade <= 25:
	print("O atleta pertence a categoria SENIOR! ")
else:
	print("O atleta pertence a categoria MASTER! ")