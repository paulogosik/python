from funcoes import *

frase = input("Informe uma frase: ")
print("-" * 30)
contaPalavras = contaTexto(frase)
for key, value in contaPalavras.items():
    print(f"A palavra {key} apareceu {value} vezes")
