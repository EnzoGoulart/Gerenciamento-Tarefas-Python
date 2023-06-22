from funcoes import *
import time
from datetime import date

dia_atual = date.today()
data_formatada = dia_atual.strftime("%d/%m/%Y")
tarefas = []
while True:
    linha()
    print('\033[0;49;36mSistema de gerenciamento de tarefas\033[m')
    linha()
    print('Digite 1 para criar tarefas')
    print('Digite 2 para alterar tarefa')
    print('Digite 3 para deletar tarefa')
    print('Digite 4 para ver tarefas')
    print('Digite 5 para \033[0;49;91msair\033[m')
    linha()
    opc = opcValida('Digite: ')
    linha()
    if opc == 1:
        nome = verificaNome()
        bio = verificaBio()
        progresso = verificaProgresso()
        p = [len(tarefas),nome,bio, data_formatada, progresso]
        tarefas.append(p)
        for c in tarefas:
            if c == p:
                print('\033[0;49;92mTarefa registrada com sucesso!\033[m')
                break
    elif opc == 2:
        linha()
        idAlt = verificaIdAlt(tarefas)
        linha()
        print('Digite 1 para alterar o nome')
        print('Digite 2 para alterar a descrição')
        opcAlt = verificaOpcAlt()
        linha()
        if opcAlt == 1:
            novoNome = verNovoNome()
            for c in tarefas:
                if c[0] == idAlt:
                    c[1] = novoNome
                    break
        elif opcAlt == 2:
            novaBio = verNovaBio()
            for c in tarefas:
                if c[0] == idAlt:
                    c[2] = novaBio
                    break
        print('\033[0;49;92mTarefa atualizada com sucesso!\033[m')
    elif opc == 3:
        opcAlt = verificaOpcDel(tarefas)
        for c in tarefas:
            if c[0] == idAlt:
                tarefas.remove(c)
                break
        print('\033[0;49;92mTarefa deletada com sucesso!\033[m')
    elif opc == 4:
        for c in tarefas:
            print(f'\033[0;49;34mid: {c[0]}   Nome: {c[1]}   Início: {c[3]} ')
            print(f'Descrição: {c[2]}')
            if progresso != 100:
                print(f'Progresso: {c[4]}\033[m')
            else: 
                print(f'\033[0;49;34mProgresso: \033[0;49;92m{c[4]}\033[m')
            if c != tarefas[-1]:
                print('-'*10)
        linha()
        print(f'\033[0;49;92mTodas as tarefas foram mostradas.\033[m')
        linha()
        time.sleep(2)
    elif opc == 5:
        break