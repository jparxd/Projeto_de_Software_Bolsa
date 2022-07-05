from Src.Aluno.Aluno import Aluno
from Src.Bolsa.Bolsa import Bolsa
from Src.Professor.Professor import Professor
from Src.selecao.selecao import Selecao
import os

#  vai ter uma id para identificar o objeto dentro da lista
#  isso utilizando o método index()

'''aluno1 = Aluno(523678)
aluno1.set_ira(9.0)
aluno1.set_nome('Filipe Sousa')
aluno2 = Aluno(524687)
aluno2.set_ira(10)
aluno2.set_nome('Ronaldinho Gaúcho')
aluno3 = Aluno(523678)
aluno3.set_ira(9.0)
aluno4 = Aluno(524687)
aluno4.set_ira(8.9)
aluno5 = Aluno(524697)
aluno5.set_ira(9.5)

professor1 = Professor(123456)
professor1.set_nome('Anderson')
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

if selecao.get_login_aluno('Filipe Sousa', 523678):
    print('Login do aluno efetuado com sucesso!')

if selecao.get_login_professor('Anderson', 123456):
    print('Login do professor efetuado com sucesso!')

# selecao.imprimir_notas()
# selecao.comparar_notas()


#  ordenação decrescente
selecao._alunos = sorted(selecao._alunos, key=lambda notas: notas._ira, reverse=True)

#  teste para printar nota do aluno
for alu in selecao._alunos:
    print(alu.get_ira())

#  para mostrar o status de cada objeto
selecao.classificado(2)
for alu in selecao._alunos:
    print(alu.get_status())

#print(selecao._alunos)
#print(selecao._professores)
#print('\n')
aluno1.imprimir()


bolsa = Bolsa("Futebol")
bolsa1 = Bolsa("Basquete")
selecao.cadastrar_bolsa(bolsa)
#selecao.cadastrar_bolsa(bolsa)
selecao.cadastrar_bolsa(bolsa1)
#bolsa.preencher_bolsa(aluno1)
bolsa.preencher_bolsa(aluno2)
bolsa1.preencher_bolsa(aluno3)
#selecao.escolher_bolsas()
selecao.mostrar_bolsas()
selecao.escolher_bolsas(bolsa,aluno1)
selecao.escolher_bolsas(bolsa,aluno1)
print("+-*/"*30)
selecao.mostrar_bolsas()
'''
if __name__ == '__main__':
#manu principal
    selecao = Selecao()
    while (True):
        op = int(input('[1] - CADASTRO\n'
                       '[2] - LOGIN\n'))
        if op == 1:
            flag = True
            #os.system('cls' if os.name == 'nt' else 'clear')
            while (flag == True):
                newop = int(input('[1] - PROFESSOR\n'
                                  '[2] - ALUNO\n'))
#cadastrar professor
                if newop == 1:
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    flag = False
                    professor = Professor(int(input('SIAP: ')))
                    professor.set_nome(input('NAME: '))
                    selecao.cadastrar_professor(professor)
                    while (op != 2):
                        # os.system('cls' if os.name == 'nt' else 'clear')
                        op = int(input('DESEJA CADASTRAR BOLSA\n'
                                       '[1] - SIM\n'
                                       '[2] - NO\n'))
                        if op == 1:
                            bolsa = Bolsa(input('BOLSA A SER CADASTRADA: '))
                            selecao.cadastrar_bolsa(bolsa)

#cadastrar aluno
                elif newop == 2:
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    flag = False
                    aluno = Aluno(int(input('MATRICULA: ')))
                    aluno.set_nome(input('NOME: '))
                    aluno.set_curso(input('CURSO: '))
                    aluno.set_ira(float(input('IRA: ')))
                    selecao.cadastrar_aluno(aluno)
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    print('BOLSAS DISPONIVEIS\n')
                    selecao.mostrar_bolsas_alunos()
                    while (op != 2):

                        op = int(input('DESEJA SE CADASTRAR EM ALGUMA BOLSA?\n'
                                       '[1] - SIM\n'
                                       '[2] - NÃO\n'))
                        if op == 1:
                            nome = input('NOME DA BOLSA QUE DESEJA CADASTRAR: ')
                            selecao.escolher_bolsas(nome, aluno)
                            # os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    flag = False
                    print('ERROR')
                    # os.system('cls' if os.name == 'nt' else 'clear')
#menu login
        elif op == 2:
            flag = True
            while (flag == True):
                #os.system('cls' if os.name == 'nt' else 'clear')
                newop = int(input('[1] - PROFESSOR\n'
                                  '[2] - ALUNO\n'))
#login professor
                if newop == 1:
                    # os.system('cls' if os.name == 'nt' else 'clear')
                    flag = False
                    nome = input('NOME: ')
                    siap = int(input('SIAP: '))
                    if selecao.get_login_professor(nome, siap) == True:
                        selecao.mostrar_bolsas_professor()
                        selecao.alterar_status_aluno(int(input('MATRICULA DO ALUNO: ')), True)
                        os.system('pause')
                    else:
                        flag = False
                        print('CADASTRO NÃO ENCONTRADO')
#login aluno
                elif newop == 2:
                    flag = False
                    nome = input('NOME: ')
                    matricula = int(input('MATRICULA: '))
                    if selecao.get_login_aluno(nome, matricula) == True:
                        aluno.imprimir()
                        if aluno.get_status() == True:
                            print('APROVADO')

                    else:
                        flag = False
                        print('CADASTRO NÃO ENCONTRADO')
