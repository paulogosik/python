def gerar_medias(lista):
    alunos = []
    medias = []
    
    i = 0
    while i < len(lista):
        alunos.append(lista[i])
        medias.append(lista[i + 1] + lista[i + 2] / 2)       
        i += 3
        
    return alunos, medias