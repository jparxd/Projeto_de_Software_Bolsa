from Src.Bolsa.Notas import Notas
from Src.Aluno.Aluno import Aluno
from Src.selecao.selecao import Selecao


notas = Notas()

aluno = Aluno(523678)
aluno2 = Aluno(524687)
aluno.set_ira(8.5)
aluno2.set_ira(7.6)
aluno3 = Aluno(524687)
aluno3.set_ira(7.6)

selecao = Selecao()

selecao.cadastrar_aluno(aluno)
selecao.cadastrar_aluno(aluno2)
selecao.cadastrar_aluno(aluno3)

#selecao.imprimir_notas()

# print(selecao.buscar_conta_aluno(aluno.get_matricula()))

#  print(selecao._alunos)

#  selecao.comparar_notas(aluno)
#  selecao.imprimir_notas()