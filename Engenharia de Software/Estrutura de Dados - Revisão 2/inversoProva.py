class Tree:
    # Outras funções já implementadas...

    def filhos_de_pai_impar(self):
        # Imprime os valores dos nós cujo pai tem valor ímpar
        if self.raiz != None:
            self.raiz.filhos_de_pai_impar(None)

class No:
    # Outras funções já implementadas...

    def filhos_de_pai_impar(self, parent_value):
        # Imprime os valores dos nós cujo pai tem valor ímpar
        if parent_value is not None and parent_value % 2 != 0:
            print(self.info, end=" ")
        if self.esq != None:
            self.esq.filhos_de_pai_impar(self.info)
        if self.dir != None:
            self.dir.filhos_de_pai_impar(self.info)

'---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
class Tree:
    # Outras funções já implementadas...

    def descendente_mais_a_direita(self):
        # Retorna o maior valor da árvore
        if self.raiz != None:
            return self.raiz.descendente_mais_a_direita()
        return None

class No:
    # Outras funções já implementadas...

    def descendente_mais_a_direita(self):
        # Retorna o maior valor da subárvore
        if self.dir != None:
            return self.dir.descendente_mais_a_direita()
        return self.info

'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
class Tree:
    # Outras funções já implementadas...

    def imprime_maior_filho(self, valor):
        # Imprime o maior valor entre os descendentes do nó que contém o valor passado como argumento
        if self.raiz != None:
            return self.raiz.imprime_maior_filho(valor)

class No:
    # Outras funções já implementadas...

    def imprime_maior_filho(self, valor):
        # Imprime o maior valor entre os descendentes do nó que contém o valor passado como argumento
        if self.info == valor:
            maior_filho = self.descendente_mais_a_direita()
            print(maior_filho)
        elif valor < self.info:
            if self.esq != None:
                self.esq.imprime_maior_filho(valor)
        else:
            if self.dir != None:
                self.dir.imprime_maior_filho(valor)

    def descendente_mais_a_direita(self):
        # Retorna o maior valor da subárvore
        if self.dir != None:
            return self.dir.descendente_mais_a_direita()
        return self.info
    
'------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'