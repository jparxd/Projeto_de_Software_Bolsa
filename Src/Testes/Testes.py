import unittest

from Src.Aluno.Aluno import Aluno
from Src.Professor.Professor import Professor
from Src.selecao.selecao import Selecao


class MyTestCase(unittest.TestCase):

    def testar_cadastro_professor(self):
        professor = Professor(1020)
        selecao = Selecao()
        professor.set_nome("Clay")
        self.assertEqual(selecao.cadastrar_professor(professor), None)

    def testar_cadastro_aluno(self):
        aluno = Aluno(547896)
        aluno.set_nome('Porthos')
        selecao1 = Selecao()
        self.assertEqual(selecao1.cadastrar_aluno(aluno), None)

    def testar_buscar_aluno(self):
        b = Aluno(123456)
        a = Selecao()
        a.cadastrar_aluno(b)
        self.assertEqual(a.buscar_aluno(123456), b)
        self.assertEqual(a.buscar_aluno(555555), None)

    def testar_get_login_professor(self):
        c = Professor(1234)
        c.set_nome('Ben')
        d = Selecao()
        d.cadastrar_professor(c)
        self.assertEqual(d.get_login_professor('Ben', 1234), True)
        self.assertEqual(d.get_login_professor('Kane', 3456), False)

    def testar_get_login_aluno(self):
        a = Aluno(1234)
        a.set_nome("Gon")
        b = Selecao()
        b.cadastrar_aluno(a)
        self.assertEqual(b.get_login_aluno('Gon', 1234), True)
        self.assertEqual(b.get_login_aluno("Killua", 4567), False)




if __name__ == '__main__':
    unittest.main()
