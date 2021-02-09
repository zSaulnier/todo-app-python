from time import sleep as espera
from datetime import datetime as data

data_agora = data.now()
data_agora_texto = data_agora.strftime('%d/%m/%Y às %H:%M')
print('Seja bem vindo ao ToDo App!')
espera(1)
print('O que quer fazer hoje?')
while True:
    escolha = int(input('\n[1] - Criar uma nova tarefa\n[2] - Ver minhas tarefas\n[4]- Marcar Tarefa como '
                        'concluída\n[5] - Sair \nR: '))
    if escolha not in range(1, 6):
        print('Opa,essa opção não está no menu!Que tal tentar de novo?')
        espera(0.5)
    if escolha == 5:
        print('Obrigado e volte sempre!')
        break
    if escolha == 1:
        arquivotarefas = open("TAREFASTODOAPP.txt", "w")

        arquivotarefas.write('Qual o dia da sua tarefa: ')
        arquivotarefas.write((input('Data da tarefa : ')))
        arquivotarefas.write('\nQual a hora da tarefa: ')
        arquivotarefas.write(input('Que horas você quer fazer ? '))
        arquivotarefas.write('\nO que você vai fazer: ')
        arquivotarefas.write(input('Digite aqui o que deseja fazer: '))

        arquivotarefas = open("TAREFASTODOAPP.txt", "r")
        for linhas in arquivotarefas:
            print(linhas)
        arquivotarefas.close()
    if escolha == 2:
        arquivotarefas = open("TAREFASTODOAPP.txt", "r")
        for linhas in arquivotarefas:
            print(linhas)

    if escolha == 4:
        arquivotarefas = open("TAREFASTODOAPP.txt", "r")
        for linhas in arquivotarefas:
            print(linhas)

        escolha_tarefa_feita = int(input('Tem certeza que quer marcar essa tarefa como feita? [1]-SIM [2]-NÃO\nR: '))
        if escolha_tarefa_feita == 1:
            arquivotarefas = open("TAREFASTODOAPP.txt",
                                  "a+")  # sera adaptado pra escolher várias tarefa q vc podera add
            arquivotarefas.write(f'\nEssa tarefa foi marcada como concluída em {data_agora_texto} ! PARABÉNS!!')
            arquivotarefasfeitas = arquivotarefas
            arquivotarefasfeitas.close()
            print(f'\nEssa tarefa foi marcada como concluída em {data_agora_texto} ! PARABÉNS!!')


