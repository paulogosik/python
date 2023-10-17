from funcao8_3 import *

palavra = input("Informe uma palavra para verificar: ")
palindromo = is_palindrome(palavra)

if palindromo:
    print(f"A palavra \"{palavra}\" é um palíndromo!")
else:
    print(f"A palavra \"{palavra}\" não é um palíndromo!")
