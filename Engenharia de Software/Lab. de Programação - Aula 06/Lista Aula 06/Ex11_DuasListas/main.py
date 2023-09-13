import funcao # type: ignore

frase1 = input("=> Digite a frase 1: ")
frase2 = input("=> Digite a frase 2: ")
frasesConcatenadas = funcao.juntar_com_virgula(frase1, frase2)
print(f"=> As frases concatenadas ficaram: {frasesConcatenadas}")