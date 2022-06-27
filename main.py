from Src.Bolsa.Notas import Notas
from Src.Aluno.Aluno import Aluno
from Src.selecao.selecao import Selecao


notas = Notas()

aluno = Aluno(523678)
aluno2 = Aluno(524687)
aluno.set_ira(8.5)
aluno2.set_ira(7.6)

selecao = Selecao()

selecao.cadastrar_aluno(aluno)
selecao.cadastrar_aluno(aluno2)
selecao.imprimir_notas()
selecao.comparar_notas(aluno)
selecao.imprimir_notas()