from funcoesAP2 import *

frase = input("Informe uma frase: ")
print("\nExercício 01 -------------------------")
print(f"Maior palavra/palavras: {maiorPalavra(frase)}")

print("\nExercício 02 -------------------------")
print(f"Frase não corrigida: {frase}")
print(f"Frase corrigida: {corrigeMN(frase)}")

print("\nExercício 03 -------------------------")
contaPalavras = contaTexto(frase)
for palavras in contaPalavras:
    print(f"A palavra {palavras[0]} apareceu {palavras[1]} vezes")