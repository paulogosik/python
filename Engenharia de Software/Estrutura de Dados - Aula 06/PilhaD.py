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
        if not self.esta_vazia():
            self.topo = self.topo.prox
            self.quant -= 1

    def esta_vazia(self):
        return self.quant == 0

    def tamanho_atual(self):
        return self.quant

    def ver_topo(self):
        return self.topo.info

    def show(self):
        aux = self.topo
        while aux is not None:
            print(aux.info, end=' | ')
            aux = aux.prox
        print()
    
    def valida_parenteses(expressao):
        p = pilha_dinamica.pilha_dinamica()
        for i in range(len(expressao)):
            if expressao[i] == '(':
                p.push('(')
            elif expressao[i] == ')':
                if p.esta_vazia():
                    return False
            p.pop()
        return p.esta_vazia()
    
    def verifica_parenteses(expressao):
        pilha = pilha_dinamica()
        for char in expressao:
            if char in '([{':
                pilha.push(char)
            elif char in ')]}':
                if pilha.esta_vazia():
                    return False
                topo = pilha.pop()
                if (char == ')' and topo != '(') or \
                    (char == ']' and topo != '[') or \
                    (char == '}' and topo != '{'):
                    return False
        return pilha.esta_vazia()
    
    def verifica_palindromo(palavra):
        pilha = pilha_dinamica.pilha_dinamica()
        tam_palavra = len(palavra)
        for i in range(tam_palavra):
            pilha.push(palavra[i])
        for i in range(tam_palavra):
            if pilha.ver_topo() != palavra[i]:
                return False
            pilha.pop()
        return True