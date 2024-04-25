class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldsec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.ult.prox = self.prim
            # self.prim = self.ult = self.ult.prox = No(valor, None)
        else:
            self.prim = self.ult.prox = No(valor, self.prim)
        self.quant += 1

    def show(self):
        aux = self.prim
        while aux.prox != self.prim:
            print(aux.info, end=" | ")
            aux = aux.prox
        print(self.ult.info)
