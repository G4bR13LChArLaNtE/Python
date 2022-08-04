import time
import random

def jkp(n):
	if n == 0:
		n1 = "PEDRA"
	elif n == 1:
		n1 = "PAPEL"
	elif n == 2:
		n1 = "TESOURA"
		
	return (n1)

robo = random.randint(0,2)

ret1 = jkp(robo)

print("Suas opções:")
print("[ 0 ] PEDRA ")
print("[ 1 ] PAPEL ")
print("[ 2 ] TESOURA ")
n = int(input("Qual é sua jogada? "))
ret2 = jkp(n)
time.sleep(0.5)
print("JO")
time.sleep(0.5)
print("KEN")
time.sleep(0.5)
print("PO")
time.sleep(0.5)
print("-=-=-=-=-=-=-=-=-=-")

if n == robo:
	v = "Houve um Impate!"
elif n == 0 and robo == 1:
	v = "O Computador venceu!" 	
elif n== 0 and robo == 2:
	v = "O Jogador venceu!"
elif n == 1 and robo == 0:
	v = "O Jogador venceu!"
elif n == 1 and robo == 2:
	v = "O Computador venceu!"
elif n == 2 and robo == 1:
	v = "O Jogador venceu!"
elif n == 2 and robo == 0:
	v = "O Computador venceu!"
	
print("-=-=-=-=-=-=-=-=-=-")

print("O computador jogou {}".format(ret1))
print("O jogador jogou {}".format(ret2))

print("-=-=-=-=-=-=-=-=-=-")

print(v)