from funcoesAP2 import *

palavra = input("Informe uma palavra: ").upper()
if verificaPalindromo(palavra):
    print(f"A palavra {palavra} é um palíndromo")
else:
    print(f"A palavra {palavra} não é um palíndromo")