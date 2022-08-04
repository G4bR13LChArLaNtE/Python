#URI - 1166 - Pague o aluguel:

n1 = int(input())
n2 = int(input())

def calc_divida(n1,n2):
    i = 0
    while n1 > 0:
        if n1 > n2:
            i += 1
            print(f"pagamento: {i}")
            print("antes = {}".format(n1))
            n1 = n1 - n2
            print("depois = {}".format(n1))
            print("-----")
        else:
            i += 1
            print(f"pagamento: {i}")
            print("antes = {}".format(n1))
            n1 -= n1
            print(f"depois = {n1}")
            print("-----")

calc_divida(n1,n2)





