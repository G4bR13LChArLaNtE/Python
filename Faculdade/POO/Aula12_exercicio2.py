arquivo1 = open("teste1_Aula12_exercicio1.doc", "r")
soma = 0
for i in arquivo1:
    linha = int(i)
    soma += linha
print("A soma é: ", soma)

arquivo1.close()
