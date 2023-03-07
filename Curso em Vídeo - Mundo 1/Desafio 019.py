import random
print('\033[34m'
      'Você é um professor e tem que sortear entre quatro alunos para apagar o quadro.'
      '\033[m')
aln1 = input('\033[30mAluno um:\033[m')
aln2 = input('\033[30mAlundo dois:\033[m')
aln3 = input('\033[30mAluno três:\033[m')
aln4 = input('\033[30mAluno quatro:\033[m')
lista = [aln1, aln2, aln3, aln4]
res = random.choice(lista)
print('\033[34mO aluno sorteado foi:\033[34m'
      ' \033[1;33m{}\033[m'.format(res))