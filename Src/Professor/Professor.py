class Professor:
    def __init__(self, capes: int):
        self._capes = capes
        self._nome = str

    def set_capes(self, capes: int):
        self._capes = capes

    def get_capes(self):
        return self._capes

    def set_nome(self, nome: str):
        self._nome = nome

    def get_nome(self):
        return self._nome