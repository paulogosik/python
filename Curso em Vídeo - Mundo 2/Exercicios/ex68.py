from random import randint
import time
# PARTE DE INPUT
print('----------------\n'
      '=< WELCOME TO OUR [EVEN OR ODD] >=\n'
      '----------------')
while True:
    numUser = int(input('=> Type an integer number: '))
    optUser = input(f"=> Even or odd? [E/O] ").upper()
    numComp = randint(1, 20)
    
    numTotal = numUser + numComp
    
    if numTotal % 2 == 0:
        option = ['EVEN','E']
    else:
        option = ['ODD','O']
        
    print(f"-----------------")
    if optUser in option:
        print(f"=> WIN!!! You choose {numUser} and the computer choose {numComp}, that is {numTotal}. It is {option[1]}!")
    else:
        print(f"=> LOSE!!! You choose {numUser} and the computer choose {numComp}, that is {numTotal}. It is {option[1]}!")
        print(f"=> GAME OVER")
        break
    print(f"-----------------")