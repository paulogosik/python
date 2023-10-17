from funcao8_5 import *

frase = input("Informe uma frase para ser criptografada: ").lower()
rotacao = int(input("Informe um número para a rotação: "))
print("-" * 30)

fraseCorrigida = rotate_word(frase, rotacao)
print(f"Frase/palavra original: {frase}")
print(f"Frase/palavra criptografada: {fraseCorrigida}")
