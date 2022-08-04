import random 
vc= random.randint(25,180)

if vc>80 :
	mt = (vc-80)*7
	print("Você está acima do limite de velocidade, sua velocidade atual é {} Km/h, você acaba de ser multado em {} reais. ".format(vc,mt))
else: 
    print("Sua velocidade atual é {} km/h, continue a respeitar o trânsito, obrigado :) ".format(vc))
