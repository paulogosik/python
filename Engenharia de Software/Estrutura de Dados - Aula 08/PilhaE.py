class pilha_estatica:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.topo = -1

    def push(self, valor):
        self.topo += 1
        self.vetor[self.topo] = valor

    def pop(self):
        if not self.esta_vazia():
            self.topo -= 1

    def esta_vazia(self):
        return self.topo == -1

    def esta_cheia(self):
        return self.topo == self.tam_maximo - 1

    def ver_topo(self):
        return self.vetor[self.topo]

    def show(self):
        for i in range(self.topo + 1):
            print(self.vetor[i], end=' | ')
        print()

    def tamanho_atual(self):
        return self.topo + 1

    def capacidade(self):
        return self.tam_maximo
