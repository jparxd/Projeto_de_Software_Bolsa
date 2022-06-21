from Src.Bolsa.Notas import Notas
from Src.Aluno.Aluno import Aluno


notas = Notas()

aluno = Aluno(523678)
aluno2 = Aluno(524687)
aluno.set_ira(8.5)
aluno2.set_ira(9.6)

notas.adicionar_nota(aluno)
notas.adicionar_nota(aluno2)
notas.imprimir()