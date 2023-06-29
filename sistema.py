"""
Sistema que cria, altera e deleta tarefas
dá de ver as tarefas mesmo saindo pq salva no txt
tratamento de erros em todas as partes
dá de aterar tudo na tarefa, menos o ID e o dia que foi criada, que são geradas automaticamente
sempre que salva, quando abrir de novo os IDs se reoganizarão em ordem de criação
é possivel desistir de realizar uma operação no antes de concluir ela
"""



from funcoes import *
import time
from datetime import date
tarefas = []
linhas = []
array1 = []
array2 = []
id = 0
counter = 1
nomeArquivo = "tarefas.txt"


with open(nomeArquivo, "r") as arquivo:
    conteudo = arquivo.readlines()
for i in range(0, len(conteudo), 5):
    id += 1
    conteudo[i] = id
    nome = conteudo[i+1].strip()
    descricao = conteudo[i+2].strip()
    inicio = conteudo[i+3].strip()
    progresso = int(conteudo[i+4].strip())
    
    tarefa = [id, nome, descricao, inicio, progresso]
    tarefas.append(tarefa)


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
        maiorId = -1
        for item in tarefas:
            itemId = int(item[0])
            if itemId > maiorId:
                maiorId = itemId
        nome = verificaNome()
        bio = verificaBio()
        progresso = verificaProgresso()
        ctz = verCtz(f'Tem certeza que deseja criar uma nova tarefa (s/n)? ')
        if ctz in "nNNAONao":
            print('Tarefa não foi criada.')
            continue
        p = [maiorId+1,nome,bio, data_formatada, progresso]
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
            ctz = verCtz(f'Tem certeza que deseja alterar o nome da tarefa {idAlt} (s/n)? ')
            if ctz in "nNNAONao":
                print('Tarefa não foi alterada.')
                continue
            for c in tarefas:
                if c[0] == idAlt:
                    c[1] = novoNome
                    break
        elif opcAlt == 2:
            novaBio = verNovaBio()
            ctz = verCtz(f'Tem certeza que deseja alterar a descrição da tarefa {idAlt} (s/n)? ')
            if ctz in "nNNAONao":
                print('Tarefa não foi alterada.')
                continue
            for c in tarefas:
                if c[0] == idAlt:
                    c[2] = novaBio
                    break
        elif opcAlt == 3:
            novoPro = verNovoPro()
            ctz = verCtz(f'Tem certeza que deseja alterar a tarefa {idAlt} (s/n)? ')
            if ctz in "nNNAONao":
                print('Tarefa não foi alterada.')
                continue
            for c in tarefas:
                if c[0] == idAlt:
                    c[4] = novoPro
                    break
        print('\033[0;49;92mTarefa atualizada com sucesso!\033[m')
    elif opc == 3:
        opcAlt = verificaOpcDel(tarefas)
        ctz = verCtz(f'Tem certeza que deseja deletar a tarefa {opcAlt} (s/n)? ')
        if ctz in "nNNAONao":
            print('Tarefa não foi deletada.')
            continue
        for c in tarefas:
            if c[0] == opcAlt:
                tarefas.remove(c)
                break
        print('\033[0;49;92mTarefa deletada com sucesso!\033[m')
    elif opc == 4:
        for c in tarefas: 
            print(f'\033[0;49;34mid: {c[0]}   Nome: {c[1]}   Início: {c[3]} ')
            print(f'Descrição: {c[2]}')
            if int(progresso) != 100:
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