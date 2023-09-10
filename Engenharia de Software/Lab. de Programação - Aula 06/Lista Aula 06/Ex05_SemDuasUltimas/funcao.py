def sem_duas_ultimas(frase):
    fraseIncompleta = []
    palavras = frase.split(" ")
    palavras.pop(-1)
    palavras.pop(-1)
    
    return palavras