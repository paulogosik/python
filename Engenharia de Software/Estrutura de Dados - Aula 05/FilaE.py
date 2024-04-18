class fila_estatica:
    def __init__(self, tamanho):
        self.tam_maximo = tamanho
        self.vetor = [None] * tamanho
        self.quant = 0

    def inserir(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def remover(self):
        for i in range(1, self.quant):
            self.vetor[i - 1] = self.vetor[i]
        self.quant -= 1
        
    def esta_vazia(self):
        return self.quant == 0

    def esta_cheia(self):
        return self.quant == self.tam_maximo
    
    def ver_primeiro_elemento(self):
        return self.vetor[0]

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' | ')
        print()

    def tamanho_atual(self):
        return self.quant

    def capacidade(self):
        return self.tam_maximo