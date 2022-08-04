alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
          'Denise': [9.0, 8.5],
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}

'''#resultado = reprovados(alunos)
#print(resultado)'''


for i in alunos:
    lista = []
    soma = 0
    n1 = len(alunos[i])
    for j in range(n1):
        soma += alunos[i][j]
    md = soma/n1
    if md < 6:
        c = 0
        n2 = i
        lista.append(n2)
        print(n2)
        
        print(lista)
print(lista)


class Aluno:

    def __init__(self, ra, nome, turma, notas):
        self.ra = ra
        self.nome = nome
        self.turma = turma
        self.notas = notas
        notas = []

    def inserir_nota(self, nota):
        self.nota = float(input('Digite a nota: '))
        self.notas.append(nota)


aluno1 = Aluno('202101', 'João da Silva', 'SI-2')
aluno2 = Aluno('202102', 'Maria da Silva', 'SI-1')
aluno3 = Aluno('202103', 'Thiago de Paula', 'SI-3')


alunos = [aluno1, aluno2, aluno3]

aluno1.inserir_nota(10)
aluno1.inserir_nota(8)
aluno1.inserir_nota(9)
aluno1.inserir_nota(7)

aluno2.inserir_nota(7)
aluno2.inserir_nota(6)
aluno2.inserir_nota(8)

aluno3.inserir_nota(9)
aluno3.inserir_nota(7)

for i in alunos:
    media = sum(i.notas) / len(i.notas)
    print('Nome: {} - Média: {}'.format(i.nome, media))