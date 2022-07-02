from Src.Aluno.Aluno import Aluno


class Bolsa:
    def __init__(self, nome: str):
        self._nome = nome
        self.bolsa = []

    def __repr__(self):
        return f'{self._nome}: {self.bolsa}\n'

    def get_bolsa(self):
        return self._nome

    def set_nome_bolsa(self, nome: str):
        self._nome = nome

    def preencher_bolsa(self, aluno: Aluno):
        if aluno not in self.bolsa:
            self.bolsa.append(aluno)
        else:
            print("aluno ja cadastrado nessa bolsa!!")
