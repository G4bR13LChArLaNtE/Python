#URI - 1008 - Salário:

#Entradas:

n_funci = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())


#Processamento dos dados:

salario = valor_hora * horas_trabalhadas

#Saída:

print("NUMBER = {}".format(n_funci))
print("SALARY = U$ {:.2f}".format(salario))