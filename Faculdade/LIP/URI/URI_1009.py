#URI - 1009 - Salário Bônus:

#Entradas:

nome_vendedor = input()
salario = float(input())
total_vendas = float(input())

#Processamento do dados:

comissao = (total_vendas * 0.15)
total_receb = salario + comissao

#Saída:

print("TOTAL = R$ {:.2f}".format(total_receb))