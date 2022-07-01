class Professor:
    def __init__(self, siap: int):
        self._siap = siap
        self._nome = str

    def __repr__(self):
        return f"Nome: {self._nome}\nSiap: {self._siap}"

    def set_siap(self, siap: int):
        self._siap = siap

    def get_siap(self):
        return self._siap

    def set_nome(self, nome: str):
        self._nome = nome

    def get_nome(self):
        return self._nome
