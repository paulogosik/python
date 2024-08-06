'''Implemente um método que retorne o número de nós (de uma árvore binária) que
possuem pelo menos um filho'''

class Tree:
    # Outras funções já implementadas...

    def num_nos_com_filho(self):
        # Retorna o número de nós que possuem pelo menos um filho
        if self.raiz != None:
            return self.raiz.num_nos_com_filho()
        return 0

class No:
    # Outras funções já implementadas...

    def num_nos_com_filho(self):
        # Calcula o número de nós que possuem pelo menos um filho
        count = 0
        if self.esq != None or self.dir != None:
            count += 1
        if self.esq != None:
            count += self.esq.num_nos_com_filho()
        if self.dir != None:
            count += self.dir.num_nos_com_filho()
        return count

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente a função contaDescendentes(self,valor), para uma árvore binária de busca,
que retorne a quantidade de descendentes de determinado valor passado como
argumento.'''

class Tree:
    # Outras funções já implementadas...

    def contaDescendentes(self, valor):
        # Retorna a quantidade de descendentes de determinado valor
        if self.raiz != None:
            return self.raiz.contaDescendentes(valor)
        return 0

class No:
    # Outras funções já implementadas...

    def contaDescendentes(self, valor):
        # Retorna a quantidade de descendentes de determinado valor
        if self.info == valor:
            return self.quant()
        elif valor < self.info:
            if self.esq != None:
                return self.esq.contaDescendentes(valor)
        else:
            if self.dir != None:
                return self.dir.contaDescendentes(valor)
        return 0

    def quant(self):
        # Retorna a quantidade de nós na subárvore
        total = 0
        if self.esq != None:
            total += self.esq.quant() + 1
        if self.dir != None:
            total += self.dir.quant() + 1
        return total

'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente um método printCaminho que imprima todos os valores dos nós do
caminho da raiz até o nó que contém determinado valor passado como argumento.'''

class Tree:
    # Outras funções já implementadas...

    def printCaminho(self, valor):
        # Imprime todos os valores dos nós do caminho da raiz até o nó que contém o valor
        if self.raiz != None:
            self.raiz.printCaminho(valor)

class No:
    # Outras funções já implementadas...

    def printCaminho(self, valor):
        # Imprime todos os valores dos nós do caminho da raiz até o nó que contém o valor
        print(self.info, end=" ")
        if valor == self.info:
            return
        elif valor < self.info:
            if self.esq != None:
                self.esq.printCaminho(valor)
        else:
            if self.dir != None:
                self.dir.printCaminho(valor)

'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente a função somaFolhasDescendentes(self,valor), para uma árvore binária de
busca, que retorna a soma de todos os nós-folha descendentes de determinado valor
passado como argumento.'''

class Tree:
    # Outras funções já implementadas...

    def somaFolhasDescendentes(self, valor):
        # Retorna a soma de todos os nós-folha descendentes de determinado valor
        if self.raiz != None:
            return self.raiz.somaFolhasDescendentes(valor)
        return 0

class No:
    # Outras funções já implementadas...

    def somaFolhasDescendentes(self, valor):
        # Retorna a soma de todos os nós-folha descendentes de determinado valor
        if self.info == valor:
            return self.somaFolhas()
        elif valor < self.info:
            if self.esq != None:
                return self.esq.somaFolhasDescendentes(valor)
        else:
            if self.dir != None:
                return self.dir.somaFolhasDescendentes(valor)
        return 0

    def somaFolhas(self):
        # Retorna a soma dos valores dos nós folhas
        total = 0
        if self.esq == None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Considere uma árvore binária de busca que armazena valores inteiros sem repetição de
valores. Assim, os valores associados aos nós da subárvore da esquerda são menores que
o valor associado à raiz, e os valores associados à subárvore da direita são maiores ou
iguais.

a) maioresQue(x): imprime todos os valores na árvore que são maiores que x. ATENÇÃO:
A função deve tirar proveito da ordenação da árvore – caso isso não ocorra este item será
considerado pela metade.'''

class Tree:
    # Outras funções já implementadas...

    def maioresQue(self, x):
        # Imprime todos os valores na árvore que são maiores que x
        if self.raiz != None:
            self.raiz.maioresQue(x)

class No:
    # Outras funções já implementadas...

    def maioresQue(self, x):
        # Imprime todos os valores na subárvore que são maiores que x
        if self.info > x:
            if self.esq != None:
                self.esq.maioresQue(x)
            print(self.info, end=" ")
            if self.dir != None:
                self.dir.maioresQue(x)
        else:
            if self.dir != None:
                self.dir.maioresQue(x)

'''b) paiDe(x): imprime o valor do nó pai do nó que contém x (buscado a partir da raiz).'''

class Tree:
    # Outras funções já implementadas...

    def paiDe(self, x):
        # Imprime o valor do nó pai do nó que contém x
        if self.raiz != None and self.raiz.info != x:
            return self.raiz.paiDe(x, None)
        return None

class No:
    # Outras funções já implementadas...

    def paiDe(self, x, parent):
        # Imprime o valor do nó pai do nó que contém x
        if self.info == x:
            print(parent.info)
            return parent.info
        elif x < self.info:
            if self.esq != None:
                return self.esq.paiDe(x, self)
        else:
            if self.dir != None:
                return self.dir.paiDe(x, self)
        return None

'''c) imprimePares(): imprime os valores que são pares em ordem decrescente (isto é, do
maior para o menor, podendo haver repetições).'''

class Tree:
    # Outras funções já implementadas...

    def imprimePares(self):
        # Imprime os valores que são pares em ordem decrescente
        if self.raiz != None:
            self.raiz.imprimePares()

class No:
    # Outras funções já implementadas...

    def imprimePares(self):
        # Imprime os valores que são pares em ordem decrescente
        if self.dir != None:
            self.dir.imprimePares()
        if self.info % 2 == 0:
            print(self.info, end=" ")
        if self.esq != None:
            self.esq.imprimePares()

'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente um método, para uma Árvore Binária de Busca(cujos dados armazenados
são inteiros), que retorne a soma de todos os elementos da árvore'''

class Tree:
    # Outras funções já implementadas...

    def soma_elementos(self):
        # Retorna a soma de todos os elementos da árvore
        if self.raiz != None:
            return self.raiz.soma_elementos()
        return 0

class No:
    # Outras funções já implementadas...

    def soma_elementos(self):
        # Retorna a soma de todos os elementos da subárvore
        soma = self.info
        if self.esq != None:
            soma += self.esq.soma_elementos()
        if self.dir != None:
            soma += self.dir.soma_elementos()
        return soma

'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente um método, para uma Árvore Binária de Busca, que retorne o nível em que
se encontra determinado valor (passado como parâmetro). Considere o nível da raiz
como sendo 1 (um). Caso o valor não esteja na árvore, retorne zero'''

class Tree:
    # Outras funções já implementadas...

    def nivel_valor(self, valor):
        # Retorna o nível em que se encontra determinado valor
        if self.raiz != None:
            return self.raiz.nivel_valor(valor, 1)
        return 0

class No:
    # Outras funções já implementadas...

    def nivel_valor(self, valor, nivel_atual):
        # Retorna o nível em que se encontra determinado valor
        if self.info == valor:
            return nivel_atual
        elif valor < self.info:
            if self.esq != None:
                return self.esq.nivel_valor(valor, nivel_atual + 1)
        else:
            if self.dir != None:
                return self.dir.nivel_valor(valor, nivel_atual + 1)
        return 0

'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente um método, para uma Árvore Binária de Busca, que retorne o menor
elemento da árvore'''

class Tree:
    # Outras funções já implementadas...

    def menor_elemento(self):
        # Retorna o menor elemento da árvore
        if self.raiz != None:
            return self.raiz.menor_elemento()
        return None

class No:
    # Outras funções já implementadas...

    def menor_elemento(self):
        # Retorna o menor elemento da subárvore
        if self.esq != None:
            return self.esq.menor_elemento()
        return self.info

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente um método, para uma Árvore Binária, que retorne o maior elemento da
árvore'''

class Tree:
    # Outras funções já implementadas...

    def maior_elemento(self):
        # Retorna o maior elemento da árvore
        if self.raiz != None:
            return self.raiz.maior_elemento()
        return None

class No:
    # Outras funções já implementadas...

    def maior_elemento(self):
        # Retorna o maior elemento da subárvore
        if self.dir != None:
            return self.dir.maior_elemento()
        return self.info
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''Implemente um método para uma árvore binária de busca que, recebendo como
parâmetro um nó (este nó seria a raiz de uma árvore), apresente todos os elementos
desta árvore em ordem decrescente. Esta implementação deve utilizar recursividade.'''

class Tree:
    # Outras funções já implementadas...

    def imprime_decrescente(self):
        # Imprime todos os elementos da árvore em ordem decrescente
        if self.raiz != None:
            self.raiz.imprime_decrescente()

class No:
    # Outras funções já implementadas...

    def imprime_decrescente(self):
        # Imprime todos os elementos da subárvore em ordem decrescente
        if self.dir != None:
            self.dir.imprime_decrescente()
        print(self.info, end=" ")
        if self.esq != None:
            self.esq.imprime_decrescente()

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'