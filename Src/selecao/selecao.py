from Src.Aluno.Aluno import Aluno
from Src.Bolsa.Notas import Notas
from Src.Professor.Professor import Professor
from operator import attrgetter

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

    def buscar_aluno(self, matricula: int):
        for alu in self._alunos:
            if alu.get_matricula() == matricula:
                return True
        return False

    def cadastrar_aluno(self, aluno: Aluno):
        if self.buscar_aluno(aluno.get_matricula()) is False:
            self._alunos.append(aluno)

    def buscar_professor(self, capes: int):
        for prof in self._professores:
            if prof.get_capes() == capes:
                return True
        return False

    def cadastrar_professor(self, professor: Professor):
        if self.buscar_professor(professor.get_capes()) is False:
            self._professores.append(professor)

    def imprimir_notas(self):
        for alu in self._alunos:
            print(alu.get_ira())

    def get_login_professor(self):
        pass

    def get_login_aluno(self):
        pass

    def set_historico(self):
        pass

    def mostrar_arquivos_alunos(self):
        pass

    def classificado(self):
        #  o professor vai decidir quantos irão passar
        pass

    def visualizar_editais(self):
        pass

    def escolher_bolsas(self):
        pass


    def add_edital(self):
        pass

    def alterar_status_aluno(self):
        pass
