from math import sqrt
co = float(input("Qual o valor do cateto oposto? "))
ca = float(input("Qual o valor do cateto adjacente? "))
hi = (co**2 + ca**2)**(1/2)
print ("A hipotenusa irá medir {}.".format(sqrt(co**2+ca**2)))

