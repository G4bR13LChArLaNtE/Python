#Exercício 27

n = ((str(input("Digite seu nome completo: "))).strip()).split()
#  Aqui pedimos para digitar um nome coompleto, tiramos os espaços
#  dos lados e separamos os nomes em várias strings dentro da variável n.

print("Muito prazer em te conhecer!") # Utilizei uma frase para deixar o usuário mais confortável.

print("Seu primeiro nome é {}.".format(n[0])) #É mostrado seu primeiro nome.

un = int(len(n)) #Aqui é contados quantas strings há dentro da variável n.

print("Seu último nome é {}.".format(n[un - 1])) #Aqui mostramos o último nome que é un -1.

