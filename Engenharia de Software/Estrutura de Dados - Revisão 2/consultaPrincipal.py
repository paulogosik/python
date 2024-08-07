class Tree:
    def __init__(self):
        # Inicializa a árvore com a raiz como None
        self.raiz = None

    def insere(self, valor):
        # Insere um valor na árvore
        if self.raiz == None:
            self.raiz = No(valor)  # Se a raiz estiver vazia, cria um novo nó
        else:
            self.raiz.insere(valor)  # Caso contrário, insere o valor na subárvore apropriada

    def busca(self, valor):
        # Busca um valor na árvore
        if self.raiz == None:
            return False  # Retorna False se a árvore estiver vazia
        else:
            return self.raiz.busca(valor)  # Caso contrário, realiza a busca na subárvore

    def filhos_de_pai_par(self):
        # Imprime os filhos de nós cujo valor é par
        if self.raiz != None:
            self.raiz.filhos_de_pai_par()  # Chama o método na raiz

    def descendente_mais_a_esquerda(self):
        # Retorna o valor do descendente mais à esquerda na árvore
        if self.raiz != None:
            return self.raiz.descendente_mais_a_esquerda()  # Chama o método na raiz

    def imprime_menor_filho(self, valor):
        # Imprime o menor filho de um nó específico
        if self.raiz != None:
            self.raiz.imprime_menor_filho(valor)  # Chama o método na raiz


class No:
    def __init__(self, valor):
        # Inicializa um nó com um valor e ponteiros para a esquerda e direita
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        # Insere um valor na subárvore apropriada
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)  # Insere na subárvore esquerda se for menor
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)  # Insere na subárvore direita se for maior ou igual
            else:
                self.dir.insere(valor)

    def busca(self, valor):
        # Busca um valor na subárvore
        if valor == self.info:
            return True  # Valor encontrado
        elif valor < self.info:
            if self.esq == None:
                return False  # Não encontrado na subárvore esquerda
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False  # Não encontrado na subárvore direita
            else:
                return self.dir.busca(valor)

    def filhos_de_pai_par(self):
        # Imprime os filhos de nós cujo valor é par
        if self.info % 2 == 0:
            if self.esq != None:
                print(self.esq.info, end=" ")  # Imprime o valor do filho esquerdo se existir
                self.esq.filhos_de_pai_par()
            if self.dir != None:
                print(self.dir.info, end=" ")  # Imprime o valor do filho direito se existir
                self.dir.filhos_de_pai_par()
        else:
            if self.esq != None:
                self.esq.filhos_de_pai_par()  # Continua a busca na subárvore esquerda
            if self.dir != None:
                self.dir.filhos_de_pai_par()  # Continua a busca na subárvore direita

    def descendente_mais_a_esquerda(self):
        # Retorna o valor do descendente mais à esquerda
        if self.esq != None:
            return self.esq.descendente_mais_a_esquerda()  # Continua descendo à esquerda
        else:
            return self.info  # Retorna o valor do nó mais à esquerda

    def imprime_menor_filho(self, valor):
        # Imprime o menor filho de um nó específico
        if self.info == valor:
            print(self.descendente_mais_a_esquerda())  # Imprime o menor descendente à esquerda
        elif self.info > valor:
            if self.esq != None:
                self.esq.imprime_menor_filho(valor)  # Continua a busca na subárvore esquerda
        else:
            if self.dir != None:
                self.dir.imprime_menor_filho(valor)  # Continua a busca na subárvore direita
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
class Tree:
    def __init__(self):
        # Inicializa a árvore com a raiz como None
        self.raiz = None

    def insere(self, valor):
        # Insere um valor na árvore
        if self.raiz == None:
            self.raiz = No(valor)  # Se a raiz estiver vazia, cria um novo nó
        else:
            self.raiz.insere(valor)  # Caso contrário, insere o valor na subárvore apropriada

    def busca(self, valor):
        # Busca um valor na árvore
        if self.raiz == None:
            return False  # Retorna False se a árvore estiver vazia
        else:
            return self.raiz.busca(valor)  # Caso contrário, realiza a busca na subárvore

    def h(self, valor):
        # Retorna a altura do nó que contém o valor especificado
        if self.raiz != None:
            return self.raiz.h(valor) - 1  # Subtrai 1 para ajustar a altura

    def altura(self):
        # Retorna a altura da árvore
        if self.raiz != None:
            return self.raiz.altura() - 1  # Subtrai 1 para ajustar a altura

    def nivel(self, valor):
        # Retorna o nível do nó que contém o valor especificado
        if self.raiz != None:
            return self.raiz.nivel(valor)

    def printFolhas(self):
        # Imprime os valores dos nós folhas
        if self.raiz != None:
            self.raiz.printFolhas()

    def preOrdem(self):
        # Imprime a árvore em pré-ordem
        if self.raiz != None:
            print(self.raiz.info, end=" ")
            self.raiz.preOrdem()

    def contrarioPreOrdem(self):
        # Imprime a árvore em pré-ordem inversa
        if self.raiz != None:
            self.raiz.contrarioPreOrdem()

    def inOrdem(self):
        # Imprime a árvore em ordem simétrica
        if self.raiz != None:
            self.raiz.inOrdem()

    def contrarioInOrdem(self):
        # Imprime a árvore em ordem simétrica inversa
        if self.raiz != None:
            self.raiz.contrarioInOrdem()
            print(self.raiz.info, end=" ")

    def posOrdem(self):
        # Imprime a árvore em pós-ordem
        if self.raiz != None:
            self.raiz.posOrdem()
            print(self.raiz.info, end=" ")

    def contrarioPosOrdem(self):
        # Imprime a árvore em pós-ordem inversa
        if self.raiz != None:
            self.raiz.contrarioPosOrdem()
            print(self.raiz.info, end=" ")

    def descendentesDec(self, valor):
        # Imprime os descendentes de um nó em ordem decrescente
        if self.raiz != None:
            self.raiz.descendentesDec(valor)

    def maisDir(self):
        # Retorna o valor do nó mais à direita
        if self.raiz != None:
            return self.raiz.maisDir()

    def maisEsq(self):
        # Retorna o valor do nó mais à esquerda
        if self.raiz != None:
            return self.raiz.maisEsq()

    def soma(self):
        # Retorna a soma de todos os valores da árvore
        if self.raiz != None:
            return self.raiz.soma()

    def somaFolhas(self):
        # Retorna a soma dos valores dos nós folhas
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def printCaminho(self, valor):
        # Imprime o caminho até o nó que contém o valor especificado
        if self.raiz != None:
            self.raiz.printCaminho(valor)

    def tamanhaCaminho(self, valor):
        # Retorna o tamanho do caminho até o nó que contém o valor especificado
        if self.raiz != None:
            return self.raiz.tamanhaCaminho(valor) - 1

    def somarFolhasDescedentes(self, valor):
        # Retorna a soma dos valores dos nós folhas descendentes do nó que contém o valor especificado
        if self.raiz != None:
            return self.raiz.somarFolhasDescedentes(valor)

    def getIrmao(self, valor):
        # Retorna o valor do irmão do nó que contém o valor especificado
        if self.raiz != None and self.raiz.info != valor:
            return self.raiz.getIrmao(valor)

    def numeroPares(self):
        # Imprime os valores pares da árvore
        if self.raiz != None:
            self.raiz.numeroPares()

    def qtNumeroPares(self):
        # Retorna a quantidade de valores pares na árvore
        if self.raiz != None:
            return self.raiz.qtNumeroPares()

    def numeroParesNo(self, valor):
        # Imprime os valores pares do nó que contém o valor especificado
        if self.raiz != None:
            self.raiz.numeroParesNo(valor)

    def qtNumeroParesNo(self, valor):
        # Retorna a quantidade de valores pares do nó que contém o valor especificado
        if self.raiz != None:
            return self.raiz.qtNumeroParesNo(valor)

    def Ascendentes(self, valor):
        # Imprime os ascendentes do nó que contém o valor especificado
        if self.raiz != None:
            self.raiz.Ascendentes(valor)

    def Descendentes(self, valor):
        # Imprime os descendentes do nó que contém o valor especificado
        if self.raiz != None:
            self.raiz.Descendentes(valor)

    def qtDescendentes(self, valor):
        # Retorna a quantidade de descendentes do nó que contém o valor especificado
        if self.raiz != None:
            return self.raiz.qtDescendentes(valor)


class No:
    def __init__(self, valor):
        # Inicializa um nó com um valor e ponteiros para a esquerda e direita
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        # Insere um valor na subárvore apropriada
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)  # Insere na subárvore esquerda se for menor
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)  # Insere na subárvore direita se for maior ou igual
            else:
                self.dir.insere(valor)

    def busca(self, valor):
        # Busca um valor na subárvore
        if valor == self.info:
            return True  # Valor encontrado
        elif valor < self.info:
            if self.esq == None:
                return False  # Não encontrado na subárvore esquerda
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False  # Não encontrado na subárvore direita
            else:
                return self.dir.busca(valor)

    def nivel(self, valor):
        # Retorna o nível do nó que contém o valor especificado
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.nivel(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.nivel(valor)
                if aux != 0:
                    return 1 + aux
                else:
                    return 0

    def h(self, valor):
        # Retorna a altura do nó que contém o valor especificado
        if valor == self.info:
            return self.altura()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.h(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)

    def altura(self):
        # Retorna a altura da subárvore
        hesq = hdir = 0
        if self.esq != None:
            hesq = self.esq.altura()
        if self.dir != None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)

    def printFolhas(self):
        # Imprime os valores dos nós folhas
        if self.esq != None:
            self.esq.printFolhas()

        if self.esq == None and self.dir == None:
            print(self.info, end=" ")

        if self.dir != None:
            self.dir.printFolhas()

    def preOrdem(self):
        # Imprime a subárvore em pré-ordem
        if self.esq != None:
            print(self.esq.info, end=" ")
            self.esq.preOrdem()
        if self.dir != None:
            print(self.dir.info, end=" ")
            self.dir.preOrdem()

    def contrarioPreOrdem(self):
        # Imprime a subárvore em pré-ordem inversa
        if self.dir != None:
            self.dir.contrarioPreOrdem()
        if self.esq != None:
            self.esq.contrarioPreOrdem()

        print(self.info, end=" ")

    def inOrdem(self):
        # Imprime a subárvore em ordem simétrica
        if self.esq != None:
            self.esq.inOrdem()

        print(self.info, end=" ")

        if self.dir != None:
            self.dir.inOrdem()

    def contrarioInOrdem(self):
        # Imprime a subárvore em ordem simétrica inversa
        if self.dir != None:
            self.dir.contrarioInOrdem()

        print(self.info, end=" ")

        if self.esq != None:
            self.esq.contrarioInOrdem()

    def posOrdem(self):
        # Imprime a subárvore em pós-ordem
        if self.esq != None:
            self.esq.posOrdem()
            print(self.esq.info, end=" ")
        if self.dir != None:
            self.dir.posOrdem()
            print(self.dir.info, end=" ")

    def contrarioPosOrdem(self):
        # Imprime a subárvore em pós-ordem inversa
        if self.dir != None:
            self.dir.contrarioPosOrdem()
            print(self.dir.info, end=" ")
        if self.esq != None:
            self.esq.contrarioPosOrdem()
            print(self.esq.info, end=" ")

    def descendentesDec(self, valor):
        # Imprime os descendentes de um nó em ordem decrescente
        if valor == self.info:
            if self.dir != None:
                self.dir.decresceInOrdem()
            if self.esq != None:
                self.esq.decresceInOrdem()
        elif valor <= self.info:
            if self.esq != None:
                self.esq.descendentesDec(valor)
        else:
            if self.dir != None:
                self.dir.descendentesDec(valor)

    def maisDir(self):
        # Retorna o valor do nó mais à direita
        if self.dir != None:
            return self.dir.maisDir()
        else:
            return self.info

    def maisEsq(self):
        # Retorna o valor do nó mais à esquerda
        if self.esq != None:
            return self.esq.maisEsq()
        else:
            return self.info

    def soma(self):
        # Retorna a soma de todos os valores da subárvore
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total

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

    def printCaminho(self, valor):
        # Imprime o caminho até o nó que contém o valor especificado
        print(self.info, end=" ")
        if valor == self.info:
            pass
        elif valor < self.info:
            self.esq.printCaminho(valor)
        else:
            self.dir.printCaminho(valor)

    def tamanhaCaminho(self, valor):
        # Retorna o tamanho do caminho até o nó que contém o valor especificado
        tamanho = 0
        if self.info == valor:
            tamanho = 1
        else:
            if valor < self.info:
                if self.esq != None:
                    aux = self.esq.tamanhaCaminho(valor)
                    if aux > 0:
                        tamanho += aux + 1
            else:
                if self.dir != None:
                    aux = self.dir.tamanhaCaminho(valor)
                    if aux > 0:
                        tamanho += aux + 1
        return tamanho

    def somarFolhasDescedentes(self, valor):
        # Retorna a soma dos valores dos nós folhas descendentes do nó que contém o valor especificado
        aux = 0
        if self.info == valor:
            aux = self.somaFolhas()
        else:
            if valor < self.info:
                if self.esq != None:
                    aux = self.esq.somarFolhasDescedentes(valor)
            else:
                if self.dir != None:
                    aux = self.dir.somarFolhasDescedentes(valor)
        return aux

    def getIrmao(self, valor):
        # Retorna o valor do irmão do nó que contém o valor especificado
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq != None:
                if self.esq.info == valor:
                    if self.dir != None:
                        return self.dir.info
                else:
                    return self.esq.getIrmao(valor)
        else:
            if self.dir != None:
                if self.dir.info == valor:
                    if self.esq != None:
                        return self.esq.info
                else:
                    return self.dir.getIrmao(valor)

    def numeroPares(self):
        # Imprime os valores pares da subárvore
        if self.info % 2 == 0:
            print(self.info)
        if self.esq != None:
            self.esq.numeroPares()
        if self.dir != None:
            self.dir.numeroPares()

    def qtNumeroPares(self):
        # Retorna a quantidade de valores pares na subárvore
        qt = 0
        if self.info % 2 == 0:
            qt += 1
        if self.esq != None:
            qt += self.esq.qtNumeroPares()
        if self.dir != None:
            qt += self.dir.qtNumeroPares()
        return qt

    def numeroParesNo(self, valor):
        # Imprime os valores pares do nó que contém o valor especificado
        if self.info == valor:
            self.numeroPares()
        elif valor < self.info:
            if self.esq != None:
                self.esq.numeroParesNo(valor)
        else:
            if self.dir != None:
                self.dir.numeroParesNo(valor)

    def qtNumeroParesNo(self, valor):
        # Retorna a quantidade de valores pares do nó que contém o valor especificado
        if self.info == valor:
            return self.qtNumeroPares()
        elif valor < self.info:
            if self.esq != None:
                return self.esq.qtNumeroParesNo(valor)
        else:
            if self.dir != None:
                return self.dir.qtNumeroParesNo(valor)

    def quant(self):
        # Retorna a quantidade de nós na subárvore
        total = 0
        if self.esq != None:
            total += self.esq.quant() + 1
        if self.dir != None:
            total += self.dir.quant() + 1
        return total

    def Descendentes(self, valor):
        # Imprime os descendentes do nó que contém o valor especificado
        if self.info == valor:
            if self.esq != None:
                self.esq.inOrdem()

            if self.dir != None:
                self.dir.inOrdem()

        elif valor < self.info:
            if self.esq != None:
                self.esq.Descendentes(valor)
        else:
            if self.dir != None:
                self.dir.Descendentes(valor)

    def qtDescendentes(self, valor):
        # Retorna a quantidade de descendentes do nó que contém o valor especificado
        total = 0
        if self.info == valor:
            total = self.quant()

        elif valor < self.info:
            if self.esq != None:
                total += self.esq.qtDescendentes(valor)
        else:
            if self.dir != None:
                total += self.dir.qtDescendentes(valor)
        return total

    def Ascendentes(self, valor):
        # Imprime os ascendentes do nó que contém o valor especificado
        if self.info == valor:
            return True

        elif valor < self.info:
            if self.esq != None:
                if self.esq.Ascendentes(valor):
                    print(self.info, end=" ")
                    return True
        else:
            if self.dir != None:
                if self.dir.Ascendentes(valor):
                    print(self.info, end=" ")
                    return True
'----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
class Tree:
    # Outras funções já implementadas...

    def contarFolhas(self):
        # Conta o número de folhas na árvore
        if self.raiz != None:
            return self.raiz.contarFolhas()

    def printNosInternos(self):
        # Imprime os valores dos nós internos da árvore
        if self.raiz != None:
            self.raiz.printNosInternos()

    def verificarCompleta(self):
        # Verifica se a árvore é completa
        if self.raiz != None:
            return self.raiz.verificarCompleta()

    def verificarPerfeita(self):
        # Verifica se a árvore é perfeita
        if self.raiz != None:
            return self.raiz.verificarPerfeita()

    def somaNosInternos(self):
        # Retorna a soma dos valores dos nós internos
        if self.raiz != None:
            return self.raiz.somaNosInternos()

    def mediaValores(self):
        # Retorna a média dos valores dos nós na árvore
        if self.raiz != None:
            total, count = self.raiz.somaEContagem()
            return total / count if count > 0 else 0

    def printCaminhoRaizAteNo(self, valor):
        # Imprime o caminho da raiz até o nó que contém o valor especificado
        if self.raiz != None:
            self.raiz.printCaminhoRaizAteNo(valor)

    def printCaminhoNoAteRaiz(self, valor):
        # Imprime o caminho do nó que contém o valor especificado até a raiz
        if self.raiz != None:
            self.raiz.printCaminhoNoAteRaiz(valor)

    def verificarSubarvoreCompleta(self, valor):
        # Verifica se a subárvore que contém o valor especificado é completa
        if self.raiz != None:
            return self.raiz.verificarSubarvoreCompleta(valor)

    def verificarSubarvorePerfeita(self, valor):
        # Verifica se a subárvore que contém o valor especificado é perfeita
        if self.raiz != None:
            return self.raiz.verificarSubarvorePerfeita(valor)


class No:
    # Outras funções já implementadas...

    def contarFolhas(self):
        # Conta o número de folhas na subárvore
        if self.esq == None and self.dir == None:
            return 1
        folhas = 0
        if self.esq != None:
            folhas += self.esq.contarFolhas()
        if self.dir != None:
            folhas += self.dir.contarFolhas()
        return folhas

    def printNosInternos(self):
        # Imprime os valores dos nós internos da subárvore
        if self.esq != None or self.dir != None:
            print(self.info, end=" ")
        if self.esq != None:
            self.esq.printNosInternos()
        if self.dir != None:
            self.dir.printNosInternos()

    def verificarCompleta(self):
        # Verifica se a subárvore é completa
        if self.esq == None and self.dir == None:
            return True
        if self.esq == None or self.dir == None:
            return False
        return self.esq.verificarCompleta() and self.dir.verificarCompleta()

    def verificarPerfeita(self):
        # Verifica se a subárvore é perfeita
        if self.esq == None and self.dir == None:
            return True
        if self.esq == None or self.dir == None:
            return False
        return self.esq.altura() == self.dir.altura() and self.esq.verificarPerfeita() and self.dir.verificarPerfeita()

    def somaNosInternos(self):
        # Retorna a soma dos valores dos nós internos da subárvore
        total = 0
        if self.esq != None or self.dir != None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaNosInternos()
        if self.dir != None:
            total += self.dir.somaNosInternos()
        return total

    def somaEContagem(self):
        # Retorna a soma e a contagem dos valores dos nós na subárvore
        total = self.info
        count = 1
        if self.esq != None:
            t, c = self.esq.somaEContagem()
            total += t
            count += c
        if self.dir != None:
            t, c = self.dir.somaEContagem()
            total += t
            count += c
        return total, count

    def printCaminhoRaizAteNo(self, valor):
        # Imprime o caminho da raiz até o nó que contém o valor especificado
        print(self.info, end=" ")
        if valor < self.info and self.esq != None:
            self.esq.printCaminhoRaizAteNo(valor)
        elif valor > self.info and self.dir != None:
            self.dir.printCaminhoRaizAteNo(valor)

    def printCaminhoNoAteRaiz(self, valor):
        # Imprime o caminho do nó que contém o valor especificado até a raiz
        if self.info == valor:
            print(self.info, end=" ")
            return True
        if self.esq != None and self.esq.printCaminhoNoAteRaiz(valor):
            print(self.info, end=" ")
            return True
        if self.dir != None and self.dir.printCaminhoNoAteRaiz(valor):
            print(self.info, end=" ")
            return True
        return False

    def verificarSubarvoreCompleta(self, valor):
        # Verifica se a subárvore que contém o valor especificado é completa
        if self.info == valor:
            return self.verificarCompleta()
        if valor < self.info and self.esq != None:
            return self.esq.verificarSubarvoreCompleta(valor)
        if valor > self.info and self.dir != None:
            return self.dir.verificarSubarvoreCompleta(valor)
        return False

    def verificarSubarvorePerfeita(self, valor):
        # Verifica se a subárvore que contém o valor especificado é perfeita
        if self.info == valor:
            return self.verificarPerfeita()
        if valor < self.info and self.esq != None:
            return self.esq.verificarSubarvorePerfeita(valor)
        if valor > self.info and self.dir != None:
            return self.dir.verificarSubarvorePerfeita(valor)
        return False
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''CÓDIGOS ÍMPARES E SOMA PAR DA CLARA'''
def qtNumeroImpares(self):
    # Retorna a quantidade de valores ímpares na subárvore
    qt = 0
    if self.info % 2 != 0:
        qt += 1
    if self.esq != None:
        qt += self.esq.qtNumeroImpares()
    if self.dir != None:
        qt += self.dir.qtNumeroImpares()
    return qt

def numeroImparesNo(self, valor):
    # Imprime os valores ímpares do nó que contém o valor especificado
    if self.info == valor:
        self.numeroImpares()
    elif valor < self.info:
        if self.esq != None:
            self.esq.numeroImparesNo(valor)
    else:
        if self.dir != None:
            self.dir.numeroImparesNo(valor)

def qtNumeroImparesNo(self, valor):
    # Retorna a quantidade de valores ímpares do nó que contém o valor especificado
    if self.info == valor:
        return self.qtNumeroImpares()
    elif valor < self.info:
        if self.esq != None:
            return self.esq.qtNumeroImparesNo(valor)
    else:
        if self.dir != None:
            return self.dir.qtNumeroImparesNo(valor)

def soma_nos_impares(self):
        if self!=None:
            return self.raiz. soma_nos_impares()
        
def soma_nos_impares(self):
        total = 0
        if self.info % 2 != 0:
            total = self.info
        if self.esq is not None:
            total += self.esq.soma_nos_impares()
        if self.dir is not None:
            total += self.dir.soma_nos_impares()
        return total
'-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
class Tree:
    # Outras funções já implementadas...

    def soma_filhos_de_pais_impares(self):
        # Calcula e retorna a soma dos valores dos nós cujos pais têm valores ímpares
        if self.raiz != None:
            return self.raiz.soma_filhos_de_pais_impares(None)
        return 0

    def contar_nos(self):
        # Retorna o número total de nós na árvore
        if self.raiz != None:
            return self.raiz.contar_nos()
        return 0

    def subarvore_maior_soma(self):
        # Encontra a subárvore cuja soma dos valores dos nós é a maior possível
        if self.raiz != None:
            _, maior_no = self.raiz.subarvore_maior_soma()
            return maior_no
        return None

    def nos_com_filho_unico(self):
        # Retorna uma lista dos valores dos nós que têm exatamente um filho
        if self.raiz != None:
            return self.raiz.nos_com_filho_unico()
        return []

class No:
    # Outras funções já implementadas...

    def soma_filhos_de_pais_impares(self, parent_value):
        # Calcula e retorna a soma dos valores dos nós cujos pais têm valores ímpares
        soma = 0
        if parent_value is not None and parent_value % 2 != 0:
            soma += self.info
        if self.esq != None:
            soma += self.esq.soma_filhos_de_pais_impares(self.info)
        if self.dir != None:
            soma += self.dir.soma_filhos_de_pais_impares(self.info)
        return soma

    def contar_nos(self):
        # Conta o número total de nós na subárvore
        total = 1
        if self.esq != None:
            total += self.esq.contar_nos()
        if self.dir != None:
            total += self.dir.contar_nos()
        return total

    def subarvore_maior_soma(self):
        # Encontra a subárvore cuja soma dos valores dos nós é a maior possível
        soma_total, maior_no = self.soma(), self
        if self.esq != None:
            soma_esq, no_esq = self.esq.subarvore_maior_soma()
            if soma_esq > soma_total:
                soma_total, maior_no = soma_esq, no_esq
        if self.dir != None:
            soma_dir, no_dir = self.dir.subarvore_maior_soma()
            if soma_dir > soma_total:
                soma_total, maior_no = soma_dir, no_dir
        return soma_total, maior_no

    def nos_com_filho_unico(self):
        # Retorna uma lista dos valores dos nós que têm exatamente um filho
        nos = []
        if (self.esq == None and self.dir != None) or (self.esq != None and self.dir == None):
            nos.append(self.info)
        if self.esq != None:
            nos += self.esq.nos_com_filho_unico()
        if self.dir != None:
            nos += self.dir.nos_com_filho_unico()
        return nos

    def soma(self):
        # Calcula a soma dos valores dos nós na subárvore
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
'''IMPRIMIR NÓ TIO'''
class Tree:
    # Outras funções já implementadas...

    def get_tio(self, valor):
        # Retorna o valor do nó tio do nó que contém o valor especificado
        if self.raiz != None:
            return self.raiz.get_tio(valor, None, None)
        return None


class No:
    # Outras funções já implementadas...

    def get_tio(self, valor, parent, grandparent):
        # Retorna o valor do nó tio do nó que contém o valor especificado
        if self.info == valor:
            if grandparent != None:
                if grandparent.esq == parent and grandparent.dir != None:
                    return grandparent.dir.info
                elif grandparent.dir == parent and grandparent.esq != None:
                    return grandparent.esq.info
            return None
        elif valor < self.info:
            if self.esq != None:
                return self.esq.get_tio(valor, self, parent)
        else:
            if self.dir != None:
                return self.dir.get_tio(valor, self, parent)
        return None
'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'