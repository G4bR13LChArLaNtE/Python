vg = int(input("Qual é a distância da sua viagem? "))
if vg > 200:
	vl = (vg*0.45)
else:
	vl= (vg*0.5)
print("Você está preste a começar uma viagem de {} Km.".format(vg))
print("E o preço de sua viagem será de R${:.2f}.".format(vl))