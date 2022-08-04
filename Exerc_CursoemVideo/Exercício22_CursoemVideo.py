ni = str(input('Digite seu nome inteiro: '))
print('O seu nome com todas as letras em maúsculo é {}'.format(ni.upper()))
print('O seu nome com todas as letras minúscula é {}'.format(ni.lower()))
ni2 = ni.split()
ni2 = ni2[0]
print('Seu nome inteiro tem {} letras.'.format(len(ni.replace(" ",""))))
print('Seu primeiro nome tem {} letras.'.format(len(ni2.replace(' ',''))))