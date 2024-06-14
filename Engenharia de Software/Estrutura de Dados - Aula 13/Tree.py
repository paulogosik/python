class Tree:
    def __init__(self):
        self.raiz = None
    
    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
            
    def altura(self):
        if self.raiz != None:
            return self.raiz.altura()

class No:
    def __init__(self, valor):
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
                
    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq != None:
                return self.esq.busca(valor)
        else:
            if self.dir != None:
                return self.dir.busca(valor)
            
    def in_ordem(self):
        if self.esq != None:
            self.esq.in_ordem()
        print(self.info)
        if self.dir != None:
            self.dir.in_ordem()
            
    def altura(self):
        hesq = hdir = 0
        if self.esq != None:
            hesq = self.esq.altura()
        if self.dir != None:
            hdir = self.dir.altura()
        return 1 + max(hesq, hdir)
    
    def h(self, valor):
        if valor == self.info:
            return self.altura()
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.h(valor)
        else:
            print("continua")