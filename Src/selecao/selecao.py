from Src.Aluno.Aluno import Aluno
from Src.Bolsa.Bolsa import Bolsa
from Src.Professor.Professor import Professor

import os


class Selecao:

    def __init__(self):
        self._alunos = []
        self._professores = []
        self._editais = []
        self._bolsas = {}

    def buscar_aluno(self, matricula: int):
        for alu in self._alunos:
            if alu.get_matricula() == matricula:
                return alu
        return None

    def cadastrar_aluno(self, aluno: Aluno):
        if self.buscar_aluno(aluno.get_matricula()) is None:
            self._alunos.append(aluno)

    def buscar_professor(self, siap: int):
        for prof in self._professores:
            if prof.get_siap() == siap:
                return prof
        return None

    def cadastrar_professor(self, professor: Professor):
        if self.buscar_professor(professor.get_siap()) is None:
            self._professores.append(professor)

    def imprimir_notas(self):
        for alu in self._alunos:
            print(alu.get_ira())

    def get_login_professor(self, nome: str, siap: int):
        for prof in self._professores:
            if prof.get_nome() == nome and prof.get_siap() == siap:
                return True
        return False

    def get_login_aluno(self, nome: str, matricula: int):
        for alu in self._alunos:
            if alu.get_nome() == nome and alu.get_matricula() == matricula:
                return True
        return False

    def mostrar_arquivos_alunos(self, id: int):
        #  vai ser dentro do menu isso, vai ser feito um menu e nele será utilizado o indice para selecionar o histórico
        print(self._alunos[id].get_historico())

    def classificado(self, qnt: int):
        # o professor vai decidir quantos irão passar tava pensando em usar uma variável inteira e usar ela como
        # limite do range de um for e só mudar o status para True dos objetos(a partir da qnt de vagas liberadas no
        # edital)
        # menu irá ter nome, matrícula e status do aluno na bolsa escolhida
        for i in range(qnt):
            self._alunos[i].set_status(True)

    def visualizar_editais(self):
        for edi in self._editais:
            print(edi)

    def escolher_bolsas(self, nome: str, aluno: Aluno):
        #  Aqui o Aluno deverá escolher a bolsa que ele deseja se inscrever

        nomes_bolsas = [x.get_nome_bolsa() for x in self._bolsas.values()]

        if nome in nomes_bolsas:
            self._bolsas[nome].preencher_bolsa(aluno)



    def mostrar_bolsas_professor(self):
        for bolsa in self._bolsas:
            print(f'{self._bolsas[bolsa]}')

    def mostrar_bolsas_alunos(self):
        for i in self._bolsas:
            print(i)

    def buscar_editais(self, edital):
        # Esse método serve para verificar se não tem edital repetido
        for ed in self._editais:
            if ed == edital:
                return ed
        return None

    def add_edital(self, edital):
        #  professor vai dar um append de um arquivo edital em uma lista
        #  o nome do edital vai ser responsável por não permitir repetido
        if self.buscar_editais(edital) is None:
            self._editais.append(edital)

    def alterar_status_aluno(self, matricula, status: bool):
        for alu in self._alunos:
            if alu.get_matricula() == matricula:
                alu.set_status(status)

    def cadastrar_bolsa(self, bolsa: Bolsa):
        nome = bolsa.get_nome_bolsa()
        nomes_bolsas = [x.get_nome_bolsa() for x in self._bolsas.values()]

        if nome not in nomes_bolsas:
            self._bolsas[nome] = bolsa
        else:
            print(f'Bolsa ja existente!!')

    def imprimirp(self):
        for i in self._professores:
            print(i)
