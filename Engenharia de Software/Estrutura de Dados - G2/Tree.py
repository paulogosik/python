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
            
            
    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
        
        
    def imprime_maior_filho(self, valor):
        if self.raiz != None:
            return self.raiz.imprime_maior_filho(valor)
        
    
    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()     
        
        
    def nos_com_descendente_par(self):
        if self.raiz != None:
            return self.raiz.nos_com_descendente_par()

        
        

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
            
    
    def imprime_maior_filho(self, valor):
        if self.info == valor:
            print(self.maisdir())
        elif self.info < valor:
            if self.dir != None:
                self.dir.imprime_maior_filho(valor)
        else:
            if self.esq != None:
                self.esq.imprime_maior_filho(valor)
        
        
    def maisdir(self):
        if self.dir != None:
            return self.dir.maisdir()
        else:
            return self.info
            
        
    def nos_com_descendente_par(self):
        
        if self.esq != None:
            if self.esq.info%2==0:
                print(self.info)
            if self.esq.esq!=None:
                self.esq.nos_com_descendente_par()
        if self.dir != None:
            if self.dir.info%2==0:
                print(self.info)
            if self.dir.dir!=None:
                self.dir.nos_com_descendente_par()