import random
print('\033[30mO meu computador pensou em um número aleatório de 0 a 5, tente adivinhar!\033[m')
nmr = int(input('\033[30mNúmero:\033[m'))
lista = [0, 1, 2, 3, 4, 5]
nmrcorreto = random.choice(lista)
if nmr == nmrcorreto:
    print('\033[1;32mPARABÉNS! Você acertou! O número escolhido foi: {}\033[m'.format(nmrcorreto))
else:
    print('\033[1;31mVOCÊ ERROU! O número escolhido foi: {}\033[m'.format(nmrcorreto))