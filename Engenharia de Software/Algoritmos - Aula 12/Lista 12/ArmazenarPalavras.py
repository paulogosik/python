words = []
palavras = []
i = 0

palavra = input("=> Informe uma palavra: ")
palavra = palavra.capitalize()

while palavra != "Sair":
    
    words.append(palavra)
    
    palavra = input("=> Informe uma palavra: ")
    palavra = palavra.capitalize()

print("----------------------")
palavra = input("=> Informe uma palavra para trocar: ")
palavra = palavra.capitalize()

if palavra not in words:
    print(f"=> Palavra não encontrada na lista")

while i < len(words):
    if palavra == words[i]:
        palavras.append("ELIMINADA")
    else:
        palavras.append(words[i])
    i += 1
    
print(palavras)