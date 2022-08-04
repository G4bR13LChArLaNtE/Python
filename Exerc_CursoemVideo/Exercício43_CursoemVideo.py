peso = float(input("Digite seu peso: (Kg)  "))
altura = float(input("Digite sua altura: (m) "))

imc = peso/(altura**2)

print("Imc : {:.2f}".format(imc))

if imc < 18.5:
	print("Parabéns voceê está Abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
	print("Parabéns você está no Peso ideal.")
elif imc > 25 and imc <= 30:
	print("Tome cuidado, pois você está de Sobrepeso.")
elif imc > 30 and imc <= 40:
	print("Busque fazer algum exercício , pois você está com Obesidade.")
elif imc > 40:
	print("Procure um espacialista, pois você tem Obesidade morbida.")