class Tree:
    def __init__ (self):
        self.raiz = None

    def insere(self,valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def nos_com_descendente_par(self):
        if self.raiz != None:
            return self.raiz.nos_com_descendente_par()

    def tem_descendente_par(self, valor):
        if self.raiz != None:
            return self.raiz.tem_descendente_par(valor)
    
    def imprime_maior_filho(self, valor):
        if self.raiz != None:
            return self.raiz.imprime_maior_filho(valor)

class No:
    def __init__ (self,valor):
        self.info=valor
        self.esq=None
        self.dir=None

    def insere(self,valor):
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

    def tem_par(self):
        if self.esq != None:
            if self.esq.info % 2 == 0:
                return True
            return self.esq.tem_par()
        if self.dir != None:
            if self.dir.info % 2 == 0:
                return True
            return self.dir.tem_par()
        return False

    def nos_com_descendente_par(self):
        if self.tem_par():
            print(self.info)
        if self.esq != None:
            self.esq.nos_com_descendente_par()
        if self.dir != None:
            self.dir.nos_com_descendente_par()
        
    def tem_descendente_par(self, valor):
        if valor == self.info:
            return self.tem_par()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.tem_descendente_par(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.tem_descendente_par(valor)

    def acha_maior_filho(self):
        if self.dir != None:
            self.dir.acha_maior_filho()
        else:
            print(self.info)

    def imprime_maior_filho(self, valor):
        if valor == self.info:
            if self.dir != None:
                self.dir.acha_maior_filho()
            elif self.esq != None:
                self.esq.acha_maior_filho()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.imprime_maior_filho(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.imprime_maior_filho(valor)