arquivo = open("Ips_Aula12_exercicio4.txt", 'r')

valido = open("Ips_validos.txt", 'w')

invalido = open("Ips_invalidos.txt", 'w')


for ip in arquivo:
    lista = ip.split(".")
    n1 = int(lista[0])
    n2 = int(lista[1])
    n3 = int(lista[2])
    n4 = int(lista[3])

    if n1 >= 1 and n1 <= 255 and n2 >= 0 and n2 <= 255 and \
       n3 >= 0 and n3 <= 255 and n4 >= 0 and n4 <= 255:
        valido.write(ip)
    else:
        invalido.write(ip)

arquivo.close()
valido.close()
invalido.close()
