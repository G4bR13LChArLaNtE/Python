#Exercício 37

''' Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
 escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. '''

n1 = int(input("Digite o número: "))
conv = int(input('''Escolha uma das bases para conversão:
 [1] para binário
 [2] para octal 
 [3] para hexadecimal 
 '''))

if conv == 1:
    print('{} convertido para binário é igual {}. '.format(n1,bin(n1)[2:])) #[2:] utilizado para fatiar o número
elif conv == 2:
    print('{} convertido para octal é igual a {}. '.format(n1,oct(n1)[2:]))
elif conv == 3:
    print('{} convertido para hexadecimal é igual a {}. '.format(n1,hex(n1)[2:].upper()))#.upper utilizado para
else:                                                                                    #deixar as letras
    print('Opção invalida!')                                                             #Maiúsculas.

print("Tenha um ótimo dia! :)")