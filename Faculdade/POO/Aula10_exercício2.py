"""Exercício 02
Implemente a hierarquia de herança múltipla definida pelo diagrama UML abaixo.
Em cada classe defina um contrutor e considere que os atributos são privados.


Utilize o programa abaixo para testar as classes:
estudante = Estudante("Maria", 456789, "ADS")
funcionario = Funcionario("João", 2000)
monitor = Monitor("Paulo", 123456, "SI", 1000.0, "POO", 4)

print("Nome:", monitor.get_nome())                      # Paulo
print("Matricula:", monitor.get_matricula())            # 123456
print("Curso:", monitor.get_curso())                    # SI
print("Salario:", monitor.get_salario())                # 1000.0
print("Disciplina:", monitor.get_disciplina())          # POO
print("Carga Horaria:", monitor.get_carga_horaria())    # 4

"""


class Estudante:
    def __init__(self, nome, matricula, curso):
        self.__nome = nome
        self.__matricula = matricula
        self.__curso = curso

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_curso(self):
        return self.__curso

    def set_nome(self, nome):
        self.__nome = nome

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def set_curso(self, curso):
        self.__curso = curso


class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_nome(self, nome):
        self.__nome = nome

    def set_salario(self, salrio):
        self.__salario = salrio


class Monitor(Estudante, Funcionario):
    def __init__(self, nome, matricula, curso, salario,
                 disciplina, carga_horaria):
        Estudante.__init__(self, nome, matricula, curso)
        Funcionario.__init__(self, nome, salario)
        self.__disciplina = disciplina
        self.__carga_horaria = carga_horaria

    def get_disciplina(self):
        return self.__disciplina

    def get_carga_horaria(self):
        return self.__carga_horaria

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria


estudante = Estudante("Maria", 456789, "ADS")
funcionario = Funcionario("João", 2000)
monitor = Monitor("Paulo", 123456, "SI", 1000.0, "POO", 4)

print("Nome:", monitor.get_nome())                      # Paulo
print("Matricula:", monitor.get_matricula())            # 123456
print("Curso:", monitor.get_curso())                    # SI
print("Salario:", monitor.get_salario())                # 1000.0
print("Disciplina:", monitor.get_disciplina())          # POO
print("Carga Horaria:", monitor.get_carga_horaria())    # 4
