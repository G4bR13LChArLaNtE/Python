#Função definida como somatorio:

def somatorio(n):
    soma = 0
    natural = 1
    while natural <= n:
        soma += natural
        natural += 1
    return soma

#Função valida_usuario:

def valida_usuario(login,senha):
    login = 'teste123'
    senha = '123'
    if(login == log and senha == sen):
        print("Acesso autorizado!")
        flag = True
    else:
        print('Acesso negado!')
        flag = False

    return flag

#Função tabuleiro:

def tabuleiro(n):
    linha = 0
    while linha < n:
        coluna = 0
        while coluna < n:
            if (linha + coluna) % 2 == 0:
                print(2* chr(9608), end='')
            else:
                print(2*'',end='')
            coluna += 1
        print()
        linha += 1

#Código principal:

while True:
    n = int(input("Digite um número natural entre 0 e 100: "))
    if 0 <= n <= 100:# (n <= and n >= 100) - Utilizamos para validar a resposta do usuário
        break

somatorio(n)
print(f"A soma dos {n} primeiros números naturais é {somatorio(n)}.")


#Código do usuário e senha:

while True:
    log = input("Usuário: ")
    sen = input("Senha: ")
    f = valida_usuario(log,sen)
    if (f):
        break

#Código tabuleiro:
c = int(input("Digite o tamanho de linhas do tabuleiro: "))
tabuleiro(c)