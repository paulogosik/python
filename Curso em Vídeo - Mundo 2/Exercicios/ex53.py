char = []
reverseChar = []
phrase = input("=> Inform any phrase: ")
phraseD = phrase.replace(" ", "")
char = list(phraseD)

for c in range(len(char)-1, -1, -1):
    reverseChar.append(char[c])

print("-------------")
if char == reverseChar:
    print(f"=> The phrase '{phrase}' is a polindrome!")
else:
    print(f"=> The phrase '{phrase}' is NOT a polindrome!")