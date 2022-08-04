da = int(input("Quantos dias alugados? "))
km = float(input("Quantos quilômetros rodados? "))
vl = ((km*0.15)+(da*60))
print("O total a pagar é R${:.2f}!".format(vl))