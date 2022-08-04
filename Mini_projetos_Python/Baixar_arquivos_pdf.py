"""

    Nesse mini projeto temos um programa destinado a baixar
arquivos .pdf de um link selecionado.
    Se tivermos mais de um link na página em questão,
continuaremos a rodar o programa apertando a opção 's',
no caso de termos baixado todos os arquivos relevantes
responderemos com um 'n' e o programa irá feixar.

"""



import requests

def baixar_pdf(url, endereco):
    resposta = requests.get(url)
    try:
        if resposta.status_code == requests.codes.OK:
            with open(endereco, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
                print("Download finalizado. Salvo em: {}".format(endereco))
    except:
        resposta.raise_for_status()

op = True
cont = 1

if __name__ == "__main__":
    while(op):
        url = input("Qual é o endereço da página do arquivo em questão? ")
        print()
        baixar_pdf(url, f"novo_arquivo{cont}.pdf")
        print()
        print("Por favor, mude o nome do seu novo arquivo para não termos conflito na próxima vez que usar nosso programa.")
        print()
        op = input("Você gostario de continuar? s ou n? ")
        if (op == "s"):
            op = True
            cont += 1
        else:
            op = False