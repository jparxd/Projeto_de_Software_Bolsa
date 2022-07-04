# O aluno poderá se inscrever em várias bolsas, porém, apenas uma deverá ser escolhida
class Aluno:
    def __init__(self, matricula: int):
        self._matricula = matricula
        self._nome = str
        self._curso = str
        self._ira = float
        self._status = False
        self._historico = None

    def __repr__(self):
        return f'\nNome: {self._nome}\nMatricula: {self._matricula}\nCurso: {self._curso}\nIRA: {self._ira}\n' + "-------" * 5 + '\n'

    def set_matricula(self, matricula: int):
        self._matricula = matricula

    def get_matricula(self):
        return self._matricula

    def set_nome(self, nome: str):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_curso(self, curso: str):
        self._curso = curso

    def get_curso(self):
        return self._curso

    def set_ira(self, ira: float):
        self._ira = ira

    def get_ira(self):
        return self._ira

    def set_status(self, status: bool):
        self._status = status

    def get_status(self):
        return self._status

    def set_historico(self, historico):
        self._historico = historico

    def get_historico(self):
        return self._historico

    def imprimir(self):
        return print(f'Nome: {self._nome}\nMatricula: {self._matricula}\nCurso: {self._curso}\nIRA: {self._ira}')
