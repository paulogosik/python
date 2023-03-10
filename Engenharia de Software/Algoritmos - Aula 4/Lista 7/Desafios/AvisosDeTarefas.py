acordado = 8
n1 = input('=> Qual o nome da tarefa 1? ')
t1 = float(input('=> Qual a duração da tarefa 1 (em horas)? '))
n2 = input('=> Qual o nome da tarefa 2? ')
t2 = float(input('=> Qual a duração da tarefa 2 (em horas)? '))
n3 = input('=> Qual o nome da tarefa 3? ')
t3 = float(input('=> Qual a duração da tarefa 3 (em horas)? '))
print('========================')

n1 = n1.upper()
n2 = n2.upper()
n3 = n3.upper()

if (t1 + t2 + t3) <= acordado:
    print(f'=> Você tem tempo de fazer todas as tarefas!')
elif t1 < t2 < t3:
    if (t2 + t3) <= acordado:
        print(f'=> Tarefas possíveis: {n2} e {n3}.')
    elif (t1 + t2) <= acordado:
        print(f'=> Tarefas possíveis: {n1} e {n2}.')
    else:
        print(f'=> Escolha uma tarefa para realizar.')
elif t1 < t3 < t2:
    if (t3 + t2) <= acordado:
        print(f'=> Tarefas possíveis: {n3} e {n2}.')
    elif (t1 + t3) <= acordado:
        print(f'=> Tarefas possíveis: {n1} e {n3}.')
    else:
        print(f'=> Escolha uma tarefa para realizar.')
elif t2 < t1 < t3:
    if (t1 + t3) <= acordado:
        print(f'=> Tarefas possíveis: {n1} e {n3}.')
    elif (t2 + t1) <= acordado:
        print(f'=> Tarefas possíveis: {n2} e {n1}.')
    else:
        print(f'=> Escolha uma tarefa para realizar.')
elif t2 < t3 < t1:
    if (t3 + t1) <= acordado:
        print(f'=> Tarefas possíveis: {n3} e {n1}.')
    elif (t2 + t3) <= acordado:
        print(f'=> Tarefas possíveis: {n2} e {n3}.')
    else:
        print(f'=> Escolha uma tarefa para realizar.')
elif t3 < t1 < t2:
    if (t1 + t2) <= acordado:
        print(f'=> Tarefas possíveis: {n1} e {n2}.')
    elif (t3 + t1) <= acordado:
        print(f'=> Tarefas possíveis: {n3} e {n1}.')
    else:
        print(f'=> Escolha uma tarefa para realizar.')
elif t3 < t2 < t1:
    if (t2 + t1) <= acordado:
        print(f'=> Tarefas possíveis: {n2} e {n1}.')
    elif (t3 + t2) <= acordado:
        print(f'=> Tarefas possíveis: {n3} e {n2}.')
    else:
        print(f'=> Escolha uma tarefa para realizar.')
