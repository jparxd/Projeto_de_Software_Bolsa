class Bolsa:
    def __init__(self, nome: str):
        self._nome = nome


    def __repr__(self):
        return f'Bolsa: {self.get_bolsa()}\n'
    def get_bolsa(self):
        return self._nome
