from time import sleep as wait
from datetime import datetime as data

DateNow = data.now()
TextDateNow = DateNow.strftime('%d/%m/%Y às %H:%M')
print('Seja bem vindo ao ToDo App!')
wait(1)
print('O que quer fazer hoje?')
while True:
    Choice = int(input('\n[1] - Criar uma nova tarefa\n[2] - Ver minhas tarefas\n[3]- Marcar Tarefa como '
                       'concluída\n[4] - Sair \nR: '))
    if Choice not in range(1, 5):
        print('Opa,essa opção não está no menu!Que tal tentar de novo?')
        wait(0.5)

    elif Choice == 1:
        while True:
            TaskName = input('Título da tarefa: ')
            TaskFiles = open(f"tarefa_{TaskName}.txt", 'w')
            TaskFiles.write('Qual o dia da sua tarefa: ')
            TaskFiles.write((input('Data da tarefa : ')))
            TaskFiles.write('\nQual a hora da tarefa: ')
            TaskFiles.write(input('Que horas você quer fazer ? '))
            TaskFiles.write('\nO que você vai fazer: ')
            TaskFiles.write(input('Digite aqui alguns detalhes:  '))
            TaskFiles.close()
            Choice1_1 = int(input('Voltar ao menu ou cadastrar outra tarefa?: [1]-Menu\n[2]-Tarefa\nR: '))
            if Choice1_1 == 1:
                break
            elif Choice1_1 == 2:
                pass
            else:
                print('Não temos essa opção,voltando ao menu...')
                break

    elif Choice == 2:
        TaskFiles = open("TAREFASTODOAPP.txt", "r")

        TaskFiles.close()

    elif Choice == 3:
        TaskFiles = open("TAREFASTODOAPP.txt", "r")
        for Lines in TaskFiles:
            print(Lines)

            FinishTask = int(input('Tem certeza que quer marcar essa tarefa como feita? [1]-SIM [2]-NÃO\nR: '))
            if FinishTask == 1:
                TaskFiles = open("TAREFASTODOAPP.txt",
                                 "a+")  # sera adaptado pra escolher várias tarefa q vc podera add
                TaskFiles.write(f'\nEssa tarefa foi marcada como concluída em {TextDateNow} ! PARABÉNS!!')
                FinishedTasksFIle = TaskFiles

                FinishedTasksFIle.close()
                print(f'\nEssa tarefa foi marcada como concluída em {TextDateNow} ! PARABÉNS!!')
            elif FinishTask == 2:
                print('Tudo bem , volte quando encerrá-la')

    else:
        print('Obrigado e volte sempre!')
        break
