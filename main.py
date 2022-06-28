from Src.Aluno.Aluno import Aluno
from Src.Professor.Professor import Professor
from Src.selecao.selecao import Selecao

aluno1 = Aluno(523678)
aluno1.set_ira(9.0)
aluno2 = Aluno(524687)
aluno2.set_ira(10)
aluno3 = Aluno(523678)
aluno3.set_ira(9.0)
aluno4 = Aluno(524687)
aluno4.set_ira(8.9)
aluno5 = Aluno(524697)
aluno5.set_ira(7.9)


professor1 = Professor(123456)
professor2 = Professor(454621)
professor3 = Professor(123456)
professor4 = Professor(144587)


selecao = Selecao()

selecao.cadastrar_aluno(aluno1)
selecao.cadastrar_aluno(aluno2)
selecao.cadastrar_aluno(aluno3)
selecao.cadastrar_aluno(aluno4)
selecao.cadastrar_aluno(aluno5)

selecao.cadastrar_professor(professor1)
selecao.cadastrar_professor(professor2)
selecao.cadastrar_professor(professor3)
selecao.cadastrar_professor(professor4)

#selecao.imprimir_notas()
#selecao.comparar_notas()


#  ordenação decrescente
selecao._alunos = sorted(selecao._alunos, key=lambda s: s._ira, reverse=True)

for alu in selecao._alunos:
    print(alu.get_ira())


print(selecao._alunos)
print(selecao._professores)
