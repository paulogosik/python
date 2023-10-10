def maiorPalavra(frase):
    palavras = frase.split(" ")
    palavraMaior = 0
    maioresPalavras = []
    
    for palavra in palavras:
        letras = len(palavra)
        if letras > palavraMaior:
            palavraMaior = letras
    
    for palavra in palavras:
        if len(palavra) == palavraMaior:
            maioresPalavras.append(palavra)
        
    if len(maioresPalavras) == 1:
        return ''.join(maioresPalavras)
    else:
        return maioresPalavras
    
def corrigeMN(frase):
    palavras = frase.split(" ")
    palavras_corrigidas = []
    
    for palavra in palavras:
        palavra = palavra.replace("np", "mp")
        palavra = palavra.replace("nb", "mb")
        palavras_corrigidas.append(palavra)
    
    return ' '.join(palavras_corrigidas)

def contaTexto(frase):
    palavras = frase.split(" ")
    contaPalavras = []
    palavrasVerificadas = []
    for palavra in palavras:
        if palavra not in palavrasVerificadas:
            palavrasVerificadas.append(palavra)
            listaPalavra = []
            listaPalavra.append(palavra)
            listaPalavra.append(palavras.count(palavra))
            contaPalavras.append(listaPalavra[:])
            listaPalavra.clear()
        
    return contaPalavras
        
def verificaPalindromo(palavra):
    palavraNormal = []
    palavraReverse = []
    for letra in palavra:
        palavraNormal.append(letra)
    palavraReverse = palavraNormal[:]
    palavraReverse.reverse()
    
    if palavraReverse == palavraNormal:
        return True
    else:
        return False