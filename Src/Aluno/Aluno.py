# O aluno poderá se inscrever em várias bolsas, porém, apenas uma deverá ser escolhida
class Aluno:
    def __init__(self, matricula: int):
        self._matricula = matricula
        self._nome = str
        self._curso = str
        self._ira = int

    def set_nome(self, nome: str):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_curso(self, curso: str):
        self._curso = curso

    def get_curso(self):
        return self._curso

    def set_ira(self, ira: int):
        self._ira = ira

    def get_ira(self):
        return self._ira

    def imprimir(self):
        return f'Nome: {self._nome}\nMatricula: {self._matricula}\nCurso: {self._curso}\nIRA: {self._ira}'
