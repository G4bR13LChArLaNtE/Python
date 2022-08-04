#Exercício 26

dig = str(input("Digite um nome:"))
dig = ((dig.lstrip())).lower()
print("A letra A aparece {} vezes na frase.".format(dig.count("a")))
print("A primeira letra A aparece na posição {}.".format(dig.find("a")+1))
dig = dig.rstrip()
print('A última letra A aparece na posição {}.'.format(dig.rfind("a")+1))