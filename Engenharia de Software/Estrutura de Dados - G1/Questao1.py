class No:
    def __init__(self,anterior,valor,proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo
        
class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
        
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None,valor,None)
        else:
            self.prim.ant = self.prim = No(None,valor,self.prim)
        self.quant+=1
    
    def inserir_fim(self,valor):
        if self.quant == 0:
            self.prim = self.ult = No(None,valor,None)
        else:
            self.ult.prox = self.ult = No(self.ult,valor,None)
        self.quant+=1
        
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant-=1
    
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant-=1
        
    def show(self):
        aux = self.prim
        while aux!=None:
            print(aux.info,end=' | ')
            aux = aux.prox
        print('')
        
    def show_inverso(self):
        aux = self.ult
        while aux!=None:
            print(aux.info,end=' | ')
            aux = aux.ant
        print('/n')
        
    def tamanho_atual(self):
        return self.quant

    def esta_vazia(self):
        return self.quant == 0

    def ver_primeiro(self):
        return self.prim.info

    def ver_ultimo(self):
        return self.ult.info
    
    def insere_em_ordem(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None,valor,None)
        else:
            aux = self.prim
            i = 1
            while i <= self.tamanho_atual():
                if i == self.tamanho_atual() or aux.prox == None:
                    aux.prox = No(aux, valor, None)
                    return True
                elif aux.info > valor:
                    self.prim = No(None, valor, aux)
                    self.quant += 1
                    return True
                elif aux.prox.info > valor:
                    aux.prox = aux.prox.ant = No(aux, valor, aux.prox)
                    self.quant += 1
                    return True
                aux = aux.prox
                
                i += 1