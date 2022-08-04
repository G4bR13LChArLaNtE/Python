nome = str(input("Qual seu nome?"))

if nome == ('Gabriel' or 'Michelle'):
    print("Seu nome é feio ")

elif nome == ('Pedro' or 'Maria' or 'José'):
    print("Seu nome é bem popular no Brasil")

elif nome in 'Alexandre Alves Lobo':
    print("Belo nome feminino")

else:
     print("Seu nome é normal {}".format(nome))

print("\033[1;36m","Tenha uma ótima noite {}!".format(nome) )

