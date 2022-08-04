#Aula 10

#Condicões simplea e compostas:
	
tempo = int(input("Quantos anos tem seu carro? "))

if tempo <= 3 :
	print("Seu carro está praticamente novo! :)")
else :
   print('Já está na hora de trocar! :(')
print('FIM')   

#Ou a forma simplificada:
	
tempo1 = int(input('Quantos anos tem sua moto? '))
print("Sua moto está nova!") if tempo1 <= 2 else print("Já está na hora de trocar!")
print('FIM')	
