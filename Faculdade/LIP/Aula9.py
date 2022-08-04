#Estrutura de laço de repetição While:

i = 1

while i < 6:
    print(i)
    if i == 3:
        break
    i += i
print("Fim")

a = 99

while a <= 200:
    a = a + 1
    print(a)

    if a == 200:
        break
print()
print("Fim")

b = 201
while b >= 101:
    b = b - 1
    print(b)
print()
print("Fim")

n = int(input("Digite o número: "))
m = (n - 1)+(n - 1)
c = 0

while (c <= m):
    print(c)
    c = c + 2
print("Fim")

x = int(input("Digite o primeiro número:"))
y = int(input("Digite o segundo número:"))

d = x % y
e = 0
f = 0
while ( f < x):
    if d == 0:
        e = e + 1
        f = f + y
    else:
        e = e + 1
        f = f + y
        if f > x:
            e = e - 1
print("O valor da divisão é:", e)



