import random
print('\033[4;34mEscolha a ordem de apresentação dos seus alunos.\033[m')
a1 = input('\033[30mPrimeiro aluno:\033[m')
a2 = input('\033[30mSegundo aluno:\033[m')
a3 = input('\033[30mTerceiro aluno:\033[m')
a4 = input('\033[30mQuarto aluno:\033[m')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('\033[1;33mA ordem será:\033[m')
print('\033[1;33m {}'.format(lista))