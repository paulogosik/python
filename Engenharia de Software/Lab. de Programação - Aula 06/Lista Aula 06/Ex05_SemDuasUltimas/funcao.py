def sem_duas_ultimas(frase):
    palavras = frase.split(" ")
    palavras.pop(-1)
    palavras.pop(-1)
    
    return palavras