import funcao # type: ignore

frase = input("=> Informe sua frase: ")
ultimasPalavras = funcao.duasUltimas(frase)
print(f"=> As duas últimas palavras são: {ultimasPalavras[0]} {ultimasPalavras[1]}")