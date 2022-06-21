from Src.Aluno.Aluno import Aluno


class Notas:
    def __init__(self):
        self.notas = {}

    def adicionar_nota(self, aluno: Aluno):
        self.notas[aluno.get_matricula()] = aluno.get_ira()

    def imprimir(self):
        print(self.notas)


