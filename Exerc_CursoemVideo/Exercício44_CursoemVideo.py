print("====Lojas do Charlante====")
preco = float(input("Qual é o preço da compra? R$"))
print("Formas de pagamento: ")
print("[1] à vista dinheiro/cheque")
print("[2] à vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")


while True:
	op = int(input("qual a opção? "))
	if op == 1 or op == 2 or op == 3 or op == 4:
		break


if op == 1:
    total = preco - (preco * 0.1)
elif op == 2:
	total = preco - (preco * 0.05)
elif op == 3:
	total = preco
elif op == 4:
	total = preco + (preco * 0.2)
	parcelas = int(input("Em quantas parcelas?"))
	valor_parcela = total / parcelas
	
if op == 3:
	print("Sua compra será parcelada em 2 vezes de {:.2f} sem juros.".format(total/2))
if op == 4:
	print("Sua compra será parcelada em {} vezes de {:.2f} com juros".format(parcelas,valor_parcela))

print("Sua compra de R${:.2f} no final vai custar R${:.2f}".format(preco,total))	