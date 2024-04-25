class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    # Formas de fazer sem usar o self.ult
    # def inserir_inicio(self, valor):
    #     if self.quant == 0:
    #         self.prim = No(None, valor, None)
    #     else:
    #         self.prim.ant = self.prim = No(None, valor, self.prim)
    #     self.quant += 1
    #
    # def inserir_fim(self, valor):
    #     if self.quant == 0:
    #         self.prim = No(None, valor, None)
    #     else:
    #         aux = self.prim
    #         while aux.prox is not None:
    #             aux = aux.prox
    #         aux.prox = No(aux, valor, None)
    #     self.quant += 1
