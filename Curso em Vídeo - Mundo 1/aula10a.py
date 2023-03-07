n1 = float(input('\033[1;34mDigite a sua nota do 1° Bimestre:\033[m'))
n2 = float(input('\033[1;34mDigite a sua nota do 2° Bimestre:\033[m'))
n3 = float(input('\033[1;34mDigite a sua nota do 3° Bimestre:\033[m'))
n4 = float(input('\033[1;34mDigite a sua nota do 4° Bimestre:\033[m'))
m = (n1 + n2 + n3 + n4)/4
print('\033[1;34mA sua média foi \033[m'
      '\033[4;33m{:.1f}\033[m.'.format(m))
if m >=6:
    print('\033[1;32mPARABÉNS! Você passou nessa matéria! Continue assim! ;D\033[m')
else:
    print('\033[1;31mVISH! Você não passou nessa matéria! Estude mais! :/\033[m')