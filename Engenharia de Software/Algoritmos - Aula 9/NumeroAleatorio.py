from random import randint
import os

opc = "S"

while opc == "S":
    randnumber = randint(0, 100)
    probnumber = int(input(">> Informe um possível número (entre 0 e 100): "))
    i = 1
    
    while randnumber != probnumber:
        i += 1
        
        if probnumber > randnumber:
            print(f">> Palpite maior que o número.")
        elif randnumber > probnumber:
            print(f">> Palpite menor que o número.")
        print("---------------------")
        
        probnumber = int(input(">> Informe outro possivel número: "))
    
    print("********************************")
    print(f">> Parabéns! O número é {randnumber}")
    print(f">> Quantidade de tentativas: {i}")
    print("********************************")
    opc = input(">> Deseja continuar? ").upper()
    os.system('cls' if os.name == 'nt' else 'clear')