dig = 'Curso em Video Python'
#Fatiamento de string:
print(dig[7],dig[6], dig[1])
print(dig[7]+dig[6]+dig[1])
print(dig[9:14])
print(dig[9:14:2])
print(dig[4::3])

#Análise de string:
print(len(dig)) #Tamanho da string
print(dig.count('e')) #mostra a quantidade de letras 'e' que há na variável dig
print(dig.count('o',0,13)) #mostra a quantidade de letras 'o' na variável dig entre os 13 primeiros caracteres, do 0 ao 12.
print(dig.find('deo')) #acha a palavra 'deo' dentro da variável dig e mostra o caracter que começa a palavra 'deo'.
print(dig.find('Android')) #Procura a posição que está a palavra Android dentro da string dig, quando não encontra imprime o valor -1 da podição.
print('Curso' in dig) #Imprime se é verdadeiro(truth) ou falso(false) que há a palavra curso na string dig.
#Transformação:
print(dig.replace('Python', 'Android')) #Substitui a palavra Python por Android
print(dig.upper())#Transforma todas as letras minúsculas em maiúsculas.
print(dig.lower())#Transforma as letras maiúsculas em  minúsculas. 
print(dig.capitalize()) #Transforma a primeira letra em maiúscula e as restantes em minúsculas. 
print(dig.title())#Transforma a primeira letra de cada palavra em maiúsculo e as demais letras em minúsculo.
dig2 = "   Aprenda Python"
print(dig2.strip())#Tira o espaço entre as palavras no início e no final de uma string.
print(dig2.rstrip())#Tira o espaço a direita das palavras.
print(dig2.lstrip())#Tira o espaço a esquerda das palavras.

#Divisão:
print(dig.split())#Separa as palavras da string dig
dig3 = dig.split()

#Junção:
print('-'.join(dig3))#Junta todas as palavras de dig3 e coloca - onde seria espaço.