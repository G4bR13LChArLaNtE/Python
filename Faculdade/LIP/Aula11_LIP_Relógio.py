from time import sleep

#Função relogio:

def relogio1():
    s = 0
    while s < 60:
        print(s)
        s += 1

def relogio2():
    while True:
        b = input("Quer continuar? (s/n) ")
        if b != "s":
            break
        h = 0
        while h < 24:
            m = 0
            while m < 60:
                s = 0
                while s < 60:
                    print(f'{h:02}:{m:02}:{s:02}')#{s:02} -> Imprimir o valor de s considerando 2 digitos.
                    sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000001)
                    s += 1
                m += 1
            h += 1



relogio2()



