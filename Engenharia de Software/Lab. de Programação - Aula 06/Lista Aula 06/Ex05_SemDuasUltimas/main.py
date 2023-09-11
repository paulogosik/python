import funcao # type: ignore

frase = input("=> Digite sua frase: ")
fraseIncompleta = funcao.sem_duas_ultimas(frase)
print(f"=> Frase sem as duas últimas palavras: {fraseIncompleta}")
