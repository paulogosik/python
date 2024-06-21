class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()

    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()

    def inOrdem_ao_contrario(self):
        if self.raiz != None:
            self.raiz.inOrdem_ao_contrario()

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)

    def retorna_da_raiz_ao_valor(self, valor): #Ida recursiva
        if self.raiz == None:
            return False
        else:
            return self.raiz.retorna_da_raiz_ao_valor(valor)

    def imprime_do_valor_a_raiz(self, valor): #Volta recursiva
        if self.raiz == None:
            return False
        else:
            return self.raiz.imprime_do_valor_a_raiz(valor)

    def retorna_o_nivel_do_valor_com_auxiliar(self, valor):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.retorna_o_nivel_do_valor_com_auxiliar(valor)

    def retorna_o_nivel_do_valor_sem_auxiliar(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.retorna_o_nivel_do_valor_sem_auxiliar(valor)

    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()

    def retorna_soma(self):
        if self.raiz != None:
            return self.raiz.retorna_soma()

    def retorna_soma_folhas(self):
        if self.raiz != None:
            return self.raiz.retorna_soma_folhas()

    def quantidade_de_nos_no_caminho_mais_distante(self):
        if self.raiz != None:
            return self.raiz.quantidade_de_nos_no_caminho_mais_distante()

    def h(self,valor):
        if self.raiz != None:
            return self.raiz.h(valor)

    def nivel(self,valor):
        if self.raiz != None:
            return self.raiz.nivel(valor)

    def quant(self,valor):
        if self.raiz != None:
            return self.raiz.quant(valor)

    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()

    def maisesq(self):
        if self.raiz != None:
            return self.raiz.maisesq()

    def maior_valor(self):
        if self.raiz != None:
            return self.raiz.maior_valor()

    def menor_valor(self):
        if self.raiz != None:
            return self.raiz.menor_valor()

    def retorna_descendentes_do_valor_em_ordem_crescente(self,valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.retorna_descendentes_do_valor_em_ordem_crescente(valor)

    def imprime_ancestrais(self,valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.imprime_ancestrais(valor)

    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()
    
    def soma_nos_pares(self):
        if self!=None:
            return self.raiz. soma_nos_pares()
    
    def soma_nos_impares(self):
        if self!=None:
            return self.raiz. soma_nos_impares()
    
    def contar_nos(self):
        if self!=None:
            return self.raiz. contar_nos()

    def contar_folhasnos(self):
        if self!=None:
            return self.raiz. contar_folhasnos()
    
    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()

    def retorna_se_tiver_filho(self): # Questão 1
        if self.raiz == None:
            return False
        else:
            return self.raiz.retorna_se_tiver_filho()
    
    def imprime_filhos_maiores(self,valor):
        if self.raiz!= None:
            return self.raiz.imprime_filhos_maiores(valor)
    
    def imprimirValoresPares(self):
        if self.raiz != None:
            return self.raiz.imprimirValoresPares()
            
    def imprimirValoresParesDesc(self,valor):
        if self.raiz != None:
            return self.raiz.imprimirValoresParesDesc(valor)

    def conta_descendentes(self, valor):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.conta_descendentes(valor)

    def printCaminho(self, valor):
        if self.raiz == None:
            print("Árvore vazia.")
        else:
            caminho = self.raiz.printCaminho(valor)
            if caminho:
                print(valor, caminho)
            else:
                print("Valor não encontrado na árvore.")

    def somaFolhasDescendentes(self, valor):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.somaFolhasDescendentes(valor)

    def maioresQue(self, x):
        if self.raiz != None:
            self.raiz.maioresQue(x)
    
    def paiDe(self, x):
        if self.raiz != None:
            return self.raiz.paiDe(x, None)
        return None
    
    def imprimePares(self):
        if self.raiz != None:
            pares = []
            self.raiz.coletaPares(pares)
            pares.sort(reverse=True)
            for par in pares:
                print(par, end=' ')
            print()

    def busca_nivel(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca_nivel(valor)

class No:
    def __init__(self,valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def preOrdem(self):
        print(self.info,end=' ')
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()

    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info,end=' ')
        if self.dir != None:
            self.dir.inOrdem()

    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info,end=' ')

    def inOrdem_ao_contrario(self):
        if self.dir != None:
            self.dir.inOrdem_ao_contrario()
        print(self.info,end=' ')
        if self.esq != None:
            self.esq.inOrdem_ao_contrario()
    
    
    def busca(self,valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:                
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)

    def retorna_da_raiz_ao_valor(self,valor): #Ida recursiva
        if valor == self.info:
            print(self.info)
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                print(self.info)                
                return self.esq.retorna_da_raiz_ao_valor(valor)
        else:
            if self.dir == None:
                return False
            else:
                print(self.info)
                return self.dir.retorna_da_raiz_ao_valor(valor)

    def imprime_do_valor_a_raiz(self,valor):
        if valor == self.info:
            print(self.info)
        elif valor < self.info:
            if self.esq != None:
                self.esq.imprime_do_valor_a_raiz(valor)
                print(self.info)
        else:
            if self.dir != None:
                self.dir.imprime_do_valor_a_raiz(valor)
                print(self.info)

    def retorna_o_nivel_do_valor_com_auxiliar(self,valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.retorna_o_nivel_do_valor_com_auxiliar(valor)
                if aux == 0:
                    return 0
                else:
                    return aux + 1
        else:
            aux = self.dir.retorna_o_nivel_do_valor_com_auxiliar(valor)
            if aux == 0:
                return 0
            else:
                return aux + 1

    def retorna_o_nivel_do_valor_sem_auxiliar(self,valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                return 1 + self.esq.retorna_o_nivel_do_valor_sem_auxiliar(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return 1 + self.dir.retorna_o_nivel_do_valor_sem_auxiliar(valor)

    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq == None and self.dir == None:
            print(self.info,end=' ')
        if self.dir != None:
            self.dir.printFolhas()

    def retorna_soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.retorna_soma()
        if self.dir != None:
            total += self.dir.retorna_soma()
        return total

    def retorna_soma_folhas(self):
        total = 0
        if self.esq == None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.retorna_soma_folhas()
        if self.dir != None:
            total += self.dir.retorna_soma_folhas()
        return total

    def quantidade_de_nos_no_caminho_mais_distante(self):
        hesq = hdir = 0
        if self.esq != None:
            hesq = self.esq.quantidade_de_nos_no_caminho_mais_distante()
        if self.dir != None:
            hdir = self.dir.quantidade_de_nos_no_caminho_mais_distante()
        return 1 + max(hesq,hdir)

    def h(self,valor): # Tamanho do nó contando o caminho de baixo para cima
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

    def nivel(self, valor): # Nivel ou profundidade, de um nó é o número de nós do caminho da raiz até o nó.        if valor == self.info: # O nivel da raiz, é portanto, 1.
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.nivel(valor)
                if aux != 0:
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

    def quant(self,valor): # Conta quantos nós daquele valor tem na arvore
        total = 0
        if self.info == valor:
            total += 1
        if self.esq != None:
            total += self.esq.quant(valor)
        if self.dir != None:
            total += self.dir.quant(valor)
        return total

    def maisdir(self):
        if self.dir != None:
            return self.dir.maisdir()
        else:
            return self.info

    def maisesq(self):
        if self.esq != None:
            return self.esq.maisesq()
        else:
            return self.info

    def maior_valor(self):
        if self.dir != None:
            return self.dir.maisdir()
        else:
            return self.info

    def menor_valor(self):
        if self.esq != None:
            return self.esq.maisesq()
        else:
            return self.info

    def retorna_descendentes_do_valor_em_ordem_crescente(self,valor):
        if valor == self.info:
            if self.esq != None:
                self.esq.inOrdem()
            if self.dir != None:
                self.dir.inOrdem()
        elif valor < self.info:
            if self.esq != None:
                self.esq.retorna_descendentes_do_valor_em_ordem_crescente(valor)
        else:
            if self.dir != None:
                self.dir.retorna_descendentes_do_valor_em_ordem_crescente(valor)

    def imprime_ancestrais(self,valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                aux = self.esq.imprime_ancestrais(valor)
                print(self.info)
                return aux
        else:
            if self.dir == None:
                return False
            else:
                aux = self.dir.imprime_ancestrais(valor)
                print(self.info)
                return aux
    
    def soma_nos_pares(self):
        total = 0
        if self.info % 2 == 0:
            total = self.info
        if self.esq is not None:
            total += self.esq.soma_nos_pares()
        if self.dir is not None:
            total += self.dir.soma_nos_pares()
        return total
    
    def soma_nos_impares(self):
        total = 0
        if self.info % 2 != 0:
            total = self.info
        if self.esq is not None:
            total += self.esq.soma_nos_impares()
        if self.dir is not None:
            total += self.dir.soma_nos_impares()
        return total

    def contar_folhasnos(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = 1
        if self.esq != None:
            total += self.esq.contar_folhasnos()
        if self.dir != None:
            total += self.dir.contar_folhasnos()
        return total

    def somaFolhas(self):
        total = 0
        if self.esq==None and self.dir == None:
            total = self.info
        if self.esq != None:
            total += self.esq.somaFolhas()
        if self.dir != None:
            total += self.dir.somaFolhas()
        return total
        
    def imprimirValoresPares(self):
        if self.info%2==0:
            print(self.info)
        if self.esq!=None:
            self.esq.imprimirValoresPares()
        if self.dir!=None:
            self.dir.imprimirValoresPares()

    def imprime_maior_filho(self, valor):
        if self.info == valor:
            print(self.descendente_mais_a_direita())
        elif self.info <   valor:
            if self.dir != None:
                self.dir.imprime_maior_filho(valor)
        else:
            if self.esq != None:
                self.esq.imprime_maior_filho(valor)

    def retorna_se_tiver_filho(self):
        total = 0
        if self.esq != None or self.dir != None:
            total += 1
        if self.esq != None:
            total += self.esq.retorna_se_tiver_filho()
        if self.dir!= None:
            total += self.dir.retorna_se_tiver_filho()
        return total

    
    def conta_descendentes(self, valor):
        if self.info == None:
            return 0 
        if valor == self.info:
            return self.num_descendentes()
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                return self.esq.conta_descendentes(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return self.dir.conta_descendentes(valor)

    def num_descendentes(self):
        count = 0
        if self.esq != None:
            count += 1 + self.esq.num_descendentes()
        if self.dir != None:
            count += 1 + self.dir.num_descendentes()
        return count

    def printCaminho(self, valor):
        if self == None:
            return None
        caminho = [self.info]
        if valor == self.info:
            return caminho
        elif valor < self.info:
            if self.esq == None:
                return None
            else:
                caminho_esq = self.esq.printCaminho(valor)
                if caminho_esq:
                    return caminho + caminho_esq
                else:
                    return None
        else:
            if self.dir == None:
                return None
            else:
                caminho_dir = self.dir.printCaminho(valor)
                if caminho_dir:
                    return caminho + caminho_dir
                else:
                    return None

    def somaFolhasDescendentes(self, valor):
        total = 0
        if valor == self.info:
            total += self._somaFolhas(self.esq)
            total += self._somaFolhas(self.dir)
        elif valor < self.info:
            if self.esq != None:
                total += self.esq.somaFolhasDescendentes(valor)
        else:
            if self.dir != None:
                total += self.dir.somaFolhasDescendentes(valor)
        return total
    
    def _somaFolhas(self, no):
        if no == None:
            return 0
        elif no.esq == None and no.dir == None:
            return no.info
        else:
            return self._somaFolhas(no.esq) + self._somaFolhas(no.dir)
    
    def paiDe(self, x, pai):
        if self.info == x:
            if pai != None:
                print(pai.info)
            else:
                print("Nó raiz não tem pai")
            return pai
        elif x < self.info and self.esq != None:
            return self.esq.paiDe(x, self)
        elif x > self.info and self.dir != None:
            return self.dir.paiDe(x, self)
        else:
            print("Valor não encontrado")
            return None
    
    def coletaPares(self, pares):
        if self.esq != None:
            self.esq.coletaPares(pares)
        if self.info % 2 == 0:
            pares.append(self.info)
        if self.dir != None:
            self.dir.coletaPares(pares)

    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
        return total

    def busca_nivel(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                return 1 + self.esq.busca_nivel(valor)
        else:
            if self.dir == None:
                return 0
