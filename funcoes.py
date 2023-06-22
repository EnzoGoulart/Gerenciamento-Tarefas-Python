def linha():
    print('-'*40)


def opcValida(txt):
    while True:
        try:
            opc = int(input(txt))
        except:
            print('Número inválido.')
        else:
            if opc>0 and opc<=5:
                break
            else:
                print('Opção não existe.')
    return opc


def verificaNome():
    while True:
        try:
            opc = str(input('Nome: '))
        except:
            print('Inválido.')
        else:
            if opc[0] in '123456789!@#$%¨¨&*()}{?/*-+.,':
                print('Nomes não podem começar com números ou caracteres especiais.')
            elif len(opc)>20:
                print('Excedeu 20 caracteres.')
            else:
                return opc.split()
            

def verificaBio():
    while True:
        try:
            opc = str(input('Resumo: '))
        except:
            print('Inválido.')
        else:
            return opc.split()
        

def verificaIdAlt(tarefas):
    while True:
        try:
            opc = int(input('Digite o ID da tarefa que será alterada: '))
        except:
            print('Número inválido.')
        else:
            for c in tarefas:
                if opc == c[0]:
                    return opc
                
def verificaOpcAlt():
    while True:
        try:
            opc = int(input('Digite: '))
        except:
            print('Número inválido.')
        else:
            if opc>=1 and opc<=2:
                break
            else:
                print('Opção não existe.')
    return opc

def verNovoNome():
    while True:
        try:
            opc = str(input('Novo nome: '))
        except:
            print('Inválido.')
        else:
            if opc[0] in '123456789!@#$%¨¨&*()}{?/*-+.,':
                print('Nomes não podem começar com números ou caracteres especiais.')
            elif len(opc)>20:
                print('Excedeu 20 caracteres.')
            else:
                return opc.split()
            
def verNovaBio():
     while True:
        try:
            opc = str(input('Resumo da nova descrição: '))
        except:
            print('Inválido.')
        else:
            return opc.split()
        
def verificaOpcDel(tarefas):
    while True:
        try:
            opc = int(input('Digite o ID da tarefa que será deletada: '))
            cont = 0
        except:
            print('ID inválido.')
        else:
            for c in tarefas:
                if c[0]== opc:
                    return opc 
                else:
                    cont +=1
                    if cont == len(tarefas):
                        print('ID não encontrado.')
def verificaProgresso():
    while True:
        try:
            opc = int(input('Digite o progresso da tarefa (0-100): '))
        except:
            print('Número inválido.')
        else:
            if opc>=0 and opc <=100:
                return opc