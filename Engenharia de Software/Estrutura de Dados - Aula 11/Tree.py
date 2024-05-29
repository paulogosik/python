class Tree:
    def __init__(self):
        self.raiz = None
        
    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)
            print("?")
            
class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None
        
    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
                print("*")
            else:
                self.esq.insere(valor)
                print("+")
        else:
            if self.dir == None:
                self.dir = No(valor)
                print("-")
            else:
                self.dir.insere(valor)
                print("#")