print("")
# WORD[3] --------------------------------------------------
print(f"=-=-=> ''letter = word[3]''; <=-=-=")
word  = "palavra"
letter = word[3]
print(letter)

# WHILE --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> ''while... print(word[i])''; <=-=-=")
i = 0
while i < len(word):
    print(word[i])
    i += 1

# FOR LETTER IN WORD --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> ''for letter in word''; <=-=-=")
for letter in word:
    print(letter)

# PREFIXOS --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Prefixos; <=-=-=")
prefixos = "BCDFGJLMNPRT"
sufixo = "ato"
for letra in prefixos:
    print(f"{letra}{sufixo}")
    
# SLICING --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Slicing; <=-=-=")
nomes = "Pedro, Paulo e Maria"
print(nomes[0:5])
print(nomes[7: 16])

# COMPARAÇÃO --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Comparação; <=-=-=")
# palavra = input("Digite uma palavra: ")
palavra = "teste"
if palavra < "ovo":
    print(f"=> Sua palavra ({palavra}) vem antes de ovo.")
elif palavra > "ovo":
    print(f"=> Sua palavra ({palavra}) vem depois de ovo.")
else:
    print(f"=> Sua palavra é ovo.")

# Mudando índices com função --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Mudando índices com função; <=-=-=")
palavra = "Paumas"
print(f"=> Palavra (antes): {palavra}")
palavra = palavra.replace("u", "l")
print(f"=> Palavra (depois): {palavra}")

print(f"<=>" * 4)

palavra = "Paunas"
print(f"=> Palavra (antes): {palavra}")
palavra = palavra.replace("un", "lm")
print(f"=> Palavra (depois): {palavra}")

# Procurando caracteres com função --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Procurando caracteres com função; <=-=-=")

palavra = "orangotango"
indice = palavra.find("o")
print(f"=> Letra 'o' na posição: {indice}")
print(f"=> Letra 't' na posição: {palavra.find('t')}")
print(f"=> Conjunto 'an' na posição: {palavra.find('an')}")
print(f"=> Conjunto 'an' à partir da posição [3], na posição: {palavra.find('an', 3)}")
print(f"=> Conjunto 'an' à partir da posição [3] e até a posição [7], na posição: {palavra.find('an', 3, 7)}")

# Contando algum caracter ou palavra --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Contando algum caracter ou palavra; <=-=-=")

palavra = "orangotango"

quantidade = palavra.count("o")
print(f"=> Quantidade de 'o': {quantidade}")
print(f"=> Quantidade de 'an': {palavra.count('an')}")

# UPPER() --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> UPPER() & LOWER(); <=-=-=")

texto = "MAIÚSCULA e minúscula"
print(f"=> UPPER(): {texto.upper()}")
print(f"=> LOWER(): {texto.lower()}")
print(f"=> CAPITALIZE(): {texto.capitalize()}")
print(f"=> TITLE(): {texto.title()}")
print(f"=> SWAPCASE(): {texto.swapcase()}")
print(f"=> TITLE() e SWAPCASE(): {texto.title().swapcase()}")

# Algumas verificações --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Algumas verificações <=-=-=")

texto = "maiúscula e minúscula"

if texto.islower():
    print(f"=> A frase têm apenas caracteres minúsculos")
elif texto.isupper():
    print(f"=> A frase têm apenas caracteres maiúsculos")
elif texto.istitle():
    print(f"=> A frase têm apenas as primeiras letras maiúsculas.")
if texto.isalnum():
    print(f"=> O texto contém apenas letra e números")
if texto.isalpha():
    print(f"=> O texto contém apenas letras")
if texto.isdigit():
    print(f"=> O texto contém apenas números")
if texto.startswith("m"):
    print(f"=> Começa com 'm'")
if texto.endswith("a"):
    print(f"=> Termina com 'a'")
    
# Transformando string em lista --------------------------------------------------
print(f"-" * 45)
print(f"=-=-=> Transformando string em lista <=-=-=")
texto = "Paulo Gosik Mascarenhas Moita"
texto_separado = texto.split(" ")
print(f"=> Texto: {texto}")
print(f"=> Texto separado: {texto_separado}")

print("")