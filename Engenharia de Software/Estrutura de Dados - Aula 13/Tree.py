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
        
        
    def busca0(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca0(valor)  
        
        
    def busca1(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca1(valor)
        
        
    def busca2(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
        
        
    def busca3(self, valor):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.busca(valor)
    
    
    def busca4(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca4(valor)
        
        
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()
    
    
    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()
            
    
    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()
    
    
    def h(self,valor):
        if self.raiz != None:
            return self.raiz.h(valor)
        
        
    def nivel(self, valor):
        if self.raiz != None:
            return self.raiz.nivel(valor)
        
        
    def maisdir(self):
        if self.raiz != None:
            return self.raiz.maisdir()
        
    
    def printFolhas(self):
        if self.raiz != None:
            self.raiz.printFolhas()
            
            
    def soma(self):
        if self.raiz != None:
            return self.raiz.soma()


    def somaFolhas(self):
        if self.raiz != None:
            return self.raiz.somaFolhas()




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
             
    
    def busca0(self, valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca0(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca0(valor)
    
                
    def busca1(self, valor):
        if valor == self.info:
            print(self.info)
        elif valor < self.info:
            if self.esq != None:
                print(self.info)
                return self.esq.busca1(valor)
        else:
            if self.dir != None:
                print(self.info)
                return self.dir.busca1(valor)
          
            
    def busca2(self, valor):
        if valor == self.info:
            print(self.info)
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                print(self.info)
                return self.esq.busca2(valor)
        else:
            if self.dir == None:
                return False
            else:
                print(self.info)
                return self.dir.busca2(valor)
    
    
    def busca3(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                aux = self.esq.busca3(valor)
                if aux == 0:
                    return 0
                else:
                    return aux +1
        else:
            if self.dir == None:
                return 0
            else:
                aux = self.dir.busca3(valor)
                if aux == 0:
                    return 0
                else:
                    return aux +1
               
                
    def busca4(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return 0
            else:
                return 1 + self.esq.busca4(valor)
        else:
            if self.dir == None:
                return 0
            else:
                return 1 + self.dir.busca4(valor)
          
            
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=" ")
        if self.dir != None:
            self.dir.inOrdem()
            
    
    def preOrdem(self):
        print(self.info,end=" ")
        if self.esq != None:
            self.esq.preOrdem()
        if self.dir != None:
            self.dir.preOrdem()


    def posOrdem(self):
        if self.esq != None:
            self.esq.posOrdem()
        if self.dir != None:
            self.dir.posOrdem()
        print(self.info,end=" ")
        
        
    def printFolhas(self):
        if self.esq != None:
            self.esq.printFolhas()
        if self.esq==None and self.dir == None:
            print(self.info,end=" ")
        if self.dir != None:
            self.dir.printFolhas()
            
            
    def soma(self):
        total = self.info
        if self.esq != None:
            total += self.esq.soma()
        if self.dir != None:
            total += self.dir.soma()
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
            if self.dir == None:
                return False
            else:
                return self.dir.h(valor)
    
    
    def nivel(self, valor):
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
        
        
    def quant(self,valor):
        if self.info == valor:
            total = 1
        if self.esq != None:
            total += self.esq.quant(valor)
        if self.dir != None:
            total += self.dir.quant(valor)
        return total
    
    
    def maisdir(self):
        if self.dir!=None:
            return self.dir.maisdir()
        else:
            return self.info