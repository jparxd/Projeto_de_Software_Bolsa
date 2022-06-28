from Src.Aluno.Aluno import Aluno
from Src.Professor.Professor import Professor
from Src.selecao.selecao import Selecao

aluno1 = Aluno(523678)
aluno2 = Aluno(524687)
aluno3 = Aluno(523678)
aluno4 = Aluno(524687)
aluno5 = Aluno(524697)

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


print(selecao._alunos)
print(selecao._professores)
