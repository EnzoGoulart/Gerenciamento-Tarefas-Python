from funcoes import *
import time
from datetime import date

tarefas = []
linhas = []
array1 = []
id = 0
array2 = []
counter = 1
nomeArquivo = "tarefas.txt"


with open(nomeArquivo, "r") as arquivo:
    conteudo = arquivo.readlines()

for i in range(0, len(conteudo), 5):
    id = int(conteudo[i].strip())
    nome = conteudo[i+1].strip()
    descricao = conteudo[i+2].strip()
    inicio = conteudo[i+3].strip()
    progresso = int(conteudo[i+4].strip())
    
    tarefa = [id, nome, descricao, inicio, progresso]
    tarefas.append(tarefa)

print(tarefas)


dia_atual = date.today()
data_formatada = dia_atual.strftime("%d/%m/%Y")

while True:
    linha()
    print('\033[0;49;36mSistema de gerenciamento de tarefas\033[m')
    linha()
    print('Digite 1 para criar tarefas')
    print('Digite 2 para alterar tarefa')
    print('Digite 3 para deletar tarefa')
    print('Digite 4 para ver tarefas')
    print('Digite 5 para \033[0;49;91msalvar e sair\033[m')
    linha()
    opc = opcValida('Digite: ')
    linha()
    if opc == 1:
        id = len(tarefas)
        nome = verificaNome()
        bio = verificaBio()
        progresso = verificaProgresso()
        p = [id,nome,bio, data_formatada, progresso]
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
        print('Digite 3 para alterar o progresso')
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
        elif opcAlt == 3:
            novoPro = verNovoPro()
            for c in tarefas:
                if c[0] == idAlt:
                    c[4] = novoPro
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
        nomeArquivo = "tarefas.txt"
        with open(nomeArquivo, "w") as arquivo:
            for c in tarefas:
                arquivo.write(f'{c[0]}\n {c[1]}\n {c[2]}\n {c[3]}\n {c[4]}\n')
        linha()
        print('\033[0;49;92mSalvo com sucesso, saindo...\033[m')
        linha()

        break