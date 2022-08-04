aluno_0 = [5.5, 7.0, 8.7]
aluno_1 = [8.0, 6.0, 9.2]
aluno_2 = [7.8, 8.3, 8.5]
aluno_3 = [0.0, 9.9, 9.1]

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)

media_0 = calcula_media(aluno_0)
media_1 = calcula_media(aluno_1)
media_2 = calcula_media(aluno_2)
media_3 = calcula_media(aluno_3)

print("A média do aluno 0 é: {:.2f}".format(media_0))
print("A média do aluno 1 é: {:.2f}".format(media_1))
print("A média do aluno 2 é: {:.2f}".format(media_2))
print("A média do aluno 3 é: {:.2f}".format(media_3))


alunos = [[5.5, 7.0, 8.7], [8.0, 6.0, 9.2], [7.8, 8.3, 8.5], [0.0, 9.9, 9.1]]

def calcula_medias(alunos):
    medias = []
    for aluno in alunos:
        soma = 0
        for nota in aluno:
            soma += nota
        media = soma / len(aluno)
        medias.append(media)
    return medias

medias = calcula_medias(alunos)

print()
print(format(medias))

print()

for i in range(len(medias)):
    print("A média do aluno {} é : {:.2f}".format(i, medias[i]))

