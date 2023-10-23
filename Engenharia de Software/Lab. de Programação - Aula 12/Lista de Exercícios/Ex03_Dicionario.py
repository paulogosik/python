from funcoes import *

dicionario = {
    'hello': 'olá',
    'kiss': 'beijo',
    'love': 'amor',
    'car': 'carro'
}

palavra = input("Informe uma palavra em inglês para ser traduzida: ")
print("-" * 30)
traduzir_palavra(palavra, dicionario)
