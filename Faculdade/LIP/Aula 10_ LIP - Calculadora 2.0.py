calcular = input("Deseja calcular (s/n)? ")
while calcular == "s":
    x = float(input('x: '))
    op = input('Operação: (+ - * /) ')
    y = float(input('y: '))
    if op == "+":
        resultado = x + y
    elif op == "-":
        resultado = x - y
    elif op == "*":
        resultado = x * y
    elif op == "/":
        if y == 0:
            print("Erro: Divisão por zero! \n") # \n serve para pularmos uma linha
            calcular = input("Deseja clacular (s/n)?")
            if calcular == "s":
                continue
            else:
                 break
        else:
            resultado = x/y
    print(f'{x} {op} {y} = {resultado} \n')
    calcular = input("Deseja calcular (s/n)? ")
print("Calculadora encerrada!")