#  programa seleção de bolsa

import os
#  import PyPDF2

banco_matriculas = []
banco_matriculas_professores = []
banco_nomes = []
banco_nomes_professores = []
banco_notas_alunos = []
banco_notas_alunos2 = []
banco_status_aluno = []
banco_historico = []
banco_edital = []
banco_nota_corte = []
menu = 1


#  Funções

def cadastrar_professor(nome, matricula):
    banco_nomes_professores.append(nome)
    banco_matriculas_professores.append(matricula)


def cadastrar_aluno(nome, matricula, nota, status, historico):
    banco_nomes.append(nome)
    banco_matriculas.append(matricula)
    banco_notas_alunos.append(nota)
    banco_status_aluno.append(status)
    anexar_historico(historico)



def comparar_notas(lst_nota, lst_matricula_aluno, lst_nome_aluno, lst_status_aluno, lst_historico):
    ok = False
    while not ok:
        ok = True
        for i in range(len(lst_nota) - 1):
            if lst_nota[i] < lst_nota[i + 1]:
                lst_nota[i], lst_nota[i + 1] = lst_nota[i + 1], lst_nota[i]
                lst_matricula_aluno[i], lst_matricula_aluno[i + 1] = lst_matricula_aluno[i + 1], lst_matricula_aluno[i]
                lst_nome_aluno[i], lst_nome_aluno[i + 1] = lst_nome_aluno[i + 1], lst_nome_aluno[i]
                lst_status_aluno[i], lst_status_aluno[i + 1] = lst_status_aluno[i + 1], lst_status_aluno[i]
                lst_historico[i], lst_historico[i + 1] = lst_historico[i + 1], lst_historico[i]
                ok = False


def encontrar_login_professor(nome, matricula):
    for n in banco_nomes_professores:
        if n == nome:
            if banco_matriculas_professores.index(matricula) == banco_nomes_professores.index(nome):
                print('Login efetuado com sucesso')
                return 1
            else:
                return 2


def encontrar_login_aluno(nome, matricula):
    for n in banco_nomes:
        if n == nome:
            if banco_matriculas.index(matricula) == banco_nomes.index(nome):
                print('Login efetuado com sucesso')
                return banco_nomes.index((nome))
            else:
                return None


def menu_professor():
    menu_professor = 1
    while menu_professor:
        op_prof = input('\tMenu do Professor\n1 - Anexar edital\n2 - Definir Status do Aluno\n '
        'Entre com sua resposta: ')

        if op_prof == 0:
            menu_professor = 0
        if op_prof == 1:
            caminho = input('Informe o caminho do arquivo: ')
            adicionar_edital(caminho)
        if op_prof == 2:
            alterar_status_aluno()


def menu_aluno():
    print(
        '\tMenu do Aluno\n1 - visualizar editais\n2 - Escolher bolsas\n3 - Adicionar notas\n4 - Status\n Entre com '
        'sua resposta: ')
    #  Adicionar nota ao criar a conta - check
    #  o programa vai rankear os selecionaveis - check

def status_aluno(id):
    #  diz se ele foi reprovado ou classificavel
    #  nota menor que a exigida no edital
    print(banco_status_aluno[id])


def anexar_historico(historico):
    #  para alunos classificaveis
    #  um arquivo historico.txt para ser criado
    f = open(historico)
    x = f.read()
    banco_historico.append(x)



def mostar_arquivos_alunos(id):
    #  Professor ter acesso aos documentos anexado pelos alunos
    # vai mostrar o historico para o professor
    print(banco_historico[id])


def classificado():
    #  Professor consegue alterar o status do aluno de classificavel para classificado
    #  Vai aparecer um menu com os alunos aí o professor vai escolher um aluno
    #  vai aparecer outro menu com três opções: 1 - aprovado, 2 - classificavel, 3 - reprovado

    pass


#  Funções aluno

def vizualizar_editais(lst_edital):
    #  vizualiza editais postados pelos professores
    #  o aluno vai ler o arquivo criado pelo professor(menu: o indice vai ser a opcao do menu)
     menu_edital = 1
     while menu_edital:
        op_edital = input('\tMenu Edital\n0 - Para sair do menu\n1  - Para vizualizar o primeiro edital\n2 - para vizualizar o segundo edital\nEntre com sua resposta: ')
        if op_edital == 0:
            menu_edital = 0
        if op_edital == 1:
            print(lst_edital[1])
        if op_edital == 2:
            print(lst_edital[2])

"""
    menu = 1
    while menu:
        op = input('1 - Edital 1\n2 - Edital 2\nDigite 3 para sair:\nEntre Com sua resposta: ')
        if op == 1:
            f = open('Edital1.txt')
            f.read()
            f.close()
        if op == 2:
            f = open('Edital2.txt')
            f.read()
            f.close()
        if op == 3:
            menu = 0
            """



def escolher_bolsas():
    #  para poder escolher uma bolsa eu devo ter informado as notas
    #  menu com opcoes de bolsa e que o indice da lista corresponde a leitura do edital
    menu_escolha_bolsa = 1
    while menu_escolha_bolsa:
        op_eb = input('\tMenu\n1 - Bolsa 1\n2 - Bolsa 2\nEntre com sua resposta: ')
        if op_eb == 0:
            menu_escolha_bolsa = 0
        if op_eb == 1:

            comparar_notas(banco_notas_alunos, banco_matriculas, banco_nomes, banco_status_aluno, banco_historico)
        if op_eb == 2:
            comparar_notas(banco_notas_alunos2, banco_matriculas, banco_nomes, banco_status_aluno, banco_historico)


#  Funções do Professor

def adicionar_edital(caminho_edital):
    f = open(caminho_edital)
    x = f.read()
    banco_edital.append(x)
    f.close()

def alterar_status_aluno():
    menu_altera_status = 1
    while menu_altera_status:
        qtd = len(banco_status_aluno)
        #  for status in banco_status_aluno:

    pass

while menu:

    os.system('cls')
    menu = int(input('\tMenu\n1 - Cadastrar\n2 - Login\n3 - print lista\n0 - sair\nResposta: '))
    if menu == 1:
        tipo_conta = int(input('Informe o tipo de conta que você deseja criar: 1 -  Professor / 2 - aluno: '))
        os.system('cls')

        if tipo_conta == 1:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            cadastrar_professor(nome, matricula)
            os.system('pause')
            os.system('cls')

        if tipo_conta == 2:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            status = 'Aguardando'
            historico = 'historico.txt'
            nota = 8
            cadastrar_aluno(nome, matricula, nota, status, historico)
            os.system('pause')
            os.system('cls')
            os.system('cls')

    if menu == 2:
        tipo_conta = int(input('Informe o tipo da sua conta 1 - Professor / 2 - Aluno: '))
        if tipo_conta == 1:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            encontrar_login_professor(nome, matricula)
            os.system('pause')
            os.system('cls')
            menu_professor()
            os.system('pause')
            os.system('cls')
            #  acesso a area do Professor
            #  anexa arquivos(editais)
            #  descrição dos anexos
            os.system('cls')
            pass
        if tipo_conta == 2:
            nome = input('Informe seu nome: ')
            matricula = input('informe sua matricula: ')
            id_sessao = encontrar_login_aluno(nome, matricula)
            os.system('pause')
            os.system('cls')
            #  menu
            menu_aluno()


            # encontrar_login_professor(nome, matricula)
            os.system('pause')
            os.system('cls')

            #  acesso a area do Aluno
            #  vizualiza arquivos postados pelo professor
            #  escolhe as bolsas em que quer se candidatar
            #  o aluno add suas notas ao sistema
            os.system('cls')
    if menu == 3:
        print(banco_nomes)
        os.system('pause')
