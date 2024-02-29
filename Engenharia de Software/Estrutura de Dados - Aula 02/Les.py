class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.vetor = [None] * self.tam
        self.quant = 0
        
    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
        
    def remover_fim(self):
        self.quant -= 1
    
    def esta_vazia(self):
        return self.quanto == 0
    
    def esta_cheia(self):
        return self.quant == self.tam
    
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print()
        
    def ver_primeiro(self):
        return self.vetor[0]
    
    def ver_ultimo(self):
        return self.vetor[self.quant - 1]
    
    def tamanho_atual(self):
        return self.quant
    
    def capacidade(self):
        return self.tam
    
    def inserir_inicio(self, valor):
        for i in range(self.quant, 0, -1):
            self.vetor[i] = self.vetor[i - 1]
        self.vetor[0] = valor
        self.quant += 1
        
    def remover_inicio(self):
        for i in range(self.quant - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.quant -= 1
        
    def inserir_apos(self, valor1, valor2):
        # Isere valor1 após valor2, se der. E retorne True, se não for possível retorne False.
        if self.esta_cheia() or self.essta_vazia():
            return False
        else:
            posicao_valor2 = None
            for i in range(self.quant - 1, 0, -1):
                if self.vetor[i] == valor2:
                    posicao_valor2 = i
            
            if posicao_valor2 != None:
                for i in range(self.quant, posicao_valor2 - 1, -1):
                    if i == posicao_valor2:
                        self.vetor[i + 1] = valor1
                    else:
                        self.vetor[i] = self.vetor[i - 1]
                self.quant += 1
                return True
            else: 
                return False

