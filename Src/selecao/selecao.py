from Src.Aluno.Aluno import Aluno
from Src.Bolsa.Notas import Notas
from Src.Professor.Professor import Professor

import os


class Selecao:

    def __init__(self):
        self._banco_matriculas = []
        self._banco_matriculas_professores = []
        self._banco_nomes = []
        self._banco_nomes_professores = []
        self._banco_notas_alunos = []
        self._banco_notas_alunos2 = []
        self._banco_status_aluno = []
        self._banco_historico = []
        self._banco_edital = []
        self._banco_nota_corte = []

        self._alunos = []
        self._professores = []

    def cadastrar_professor(self, professor: Professor):
        self._professores.append(professor)

    def cadastrar_aluno(self, aluno: Aluno):
        self._alunos.append(aluno)

    def comparar_notas(self):
        pass

    def get_login_professor(self):
        pass

    def get_login_aluno(self):
        pass

    def set_historico(self):
        pass

    def mostrar_arquivos_alunos(self):
        pass

    def classificado(self):
        pass

    def visualizar_editais(self):
        pass

    def escolher_bolsas(self):
        pass


    def add_edital(self):
        pass

    def alterar_status_aluno(self):
        pass
