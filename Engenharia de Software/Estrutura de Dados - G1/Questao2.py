class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class pilha_dinamica:
    def __init__(self):
        self.topo = None
        self.quant = 0

    def push(self, valor):
        self.topo = No(valor, self.topo)
        self.quant += 1

    def pop(self):
        if not self.estah_vazia():
            self.topo = self.topo.prox
            self.quant -= 1

    def estah_vazia(self):
        return self.quant == 0

    def tamanho_atual(self):
        return self.quant

    def getTopo(self):
        return self.topo.info

    def show(self):
        aux = self.topo
        while aux is not None:
            print(aux.info, end=' | ')
            aux = aux.prox
        print()
