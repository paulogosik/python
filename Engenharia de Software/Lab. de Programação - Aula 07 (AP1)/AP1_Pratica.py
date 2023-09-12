from provaG1 import * # type: ignore

lista=[12,34,21,34,13,65,21,12,13,34,21,12,12,65,57,12]

#maiorValor: 0,0625
print('O maior valor da lista é:', maiorValor(lista))

#quantidade: 0,0625
print('Quantidade de 34 na lista é:', quantidade(lista,34))

#quantidadeVarios: 0,0625
print('As quantidades de 13, 65, 15 e 57 na lista são:')
quantidadeVarios(lista,13,65,15,57)

#imprimeXValores: 0,0625
print('Os primeiros 10 valores da lista são:')
imprimePrimeirosXValores(lista,10)
print('Os primeiros 5 valores da lista são:')
imprimePrimeirosXValores(lista,5)   

#somaXValores: 0,0625
print('A soma dos 5 primeiros valores da lista é:',somaXValores(lista,5))
print('A soma dos 10 primeiros valores da lista é:',somaXValores(lista,10))

#imprimeOrdemCrescente: 0,0625
print('A lista em ordem crescente fica assim:')
imprimeOrdemCrescente(lista)

#imprimeOrdemDecrescente: 0,0625
print('A lista em ordem decrescente fica assim:')
imprimeOrdemDecrescente(lista)

#imprimeVizinhosDeX: 0,0625
print('Cada valor 12 na lista tem como vizinhos')
imprimeVizinhosDeX(lista,12)

# Bônus: +0,1 se as próximas duas linhas forem executadas corretamente conforme exemplo
print('Os primeiros 10 valores da lista são:')
imprimePrimeirosXValores(lista,10)
