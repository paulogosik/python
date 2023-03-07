import math
print('Neste programa, você digita um número com vírgula, e eu o darei a parte inteira.')
num =  float(input('Digite um número:'))
res = math.trunc(num)
print('O seu número é: {} \nA sua parte inteira é: {}'.format(num, res))