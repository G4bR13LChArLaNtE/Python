arquivo = open("teste1_Aula12_exercicio1.doc", "a", encoding="utf-8")

for i in range(10):
    num = str(input("Digite o número: "))
    arquivo.write(num + '\n')

arquivo.close()
