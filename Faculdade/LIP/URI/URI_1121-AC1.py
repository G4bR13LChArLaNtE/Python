#AC1 - Comprando com desconto:

preco = float(input())
quant = int(input())

total1 = (preco * quant)
n1 = 0.1
n2 = (0.01 * quant)
total2 = (total1 * (1 - n1 - n2))

print("{:.2f}".format(total1))
print("{:.2f}".format(total2))

