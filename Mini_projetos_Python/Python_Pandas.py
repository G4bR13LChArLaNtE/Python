#Aqui temos um teste da biblioteca pandas:

import pandas as pd

lista = ['Ferrari', 'Ford', 'Alfa Romeo', 'Chevrolet', 'Volkswagen', 'Fiat', 'Volvo', 'Nisan', 'Honda', 'Toyota']

#Utilizando a biblioteca Pandas:
s1 = pd.Series(lista, name='Marcas de carros')

print(lista)
print(s1)

print()
#Utilizando o metodo enumerate:
for key, value in enumerate(lista):
    print(key, value)