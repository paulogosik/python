from random import randint
import time
import os

items = ['Rock', 'Paper', 'Scissors']
# PARTE DE INPUT
print('----------------\n'
      '=< WELCOME TO OUR R.P.S. >=\n'
      '----------------\n'
      '=> You have three options:\n'
      '     [0] Rock\n'
      '     [1] Paper\n'
      '     [2] Scissors\n'
      '     [Others numbers] Exit')
option = int(input('=> '))

while option == 0 or option == 1 or option == 2:
      #PRA FICAR BONITINHO
      print('================')
      print('ROCK!')
      time.sleep(0.5)
      print('PAPER!')
      time.sleep(0.5)
      print('SCISSORS!')
      print('================')
      time.sleep(0.5)
      os.system('cls' if os.name == 'nt' else 'clear')

      # ORGANIZAR VARIÁVEIS E INTERPRETAR CÓDIGOS
      comp = randint(0, 2)
      optionC = items[comp]
      optionU = items[option]

      # PROCESSAMENTO DO PROGRAMA
      if optionC == optionU: # CASO HAJA EMPATE
            print(f'<! TIE !>\n'
                  f'=> User: {optionU}\n'
                  f'=> Computer: {optionC}')
      elif optionU == 'Rock': # USUÁRIO ESCOLHEU PEDRA
            if optionC == 'Paper':
                  print(f'<! COMPUTER WINS !>\n'
                        f'=> User: {optionU}\n'
                        f'=> Computer: {optionC}')
            elif optionC == 'Scissors':
                  print(f'<! USER WINS !>\n'
                        f'=> User: {optionU}\n'
                        f'=> Computer: {optionC}')
            else:
                  print('<! INVALID PLAY !>')
      elif optionU == 'Paper': # USUÁRIO ESCOLHEU PAPEL
            if optionC == 'Rock':
                  print(f'<! USER WINS !>\n'
                        f'=> User: {optionU}\n'
                        f'=> Computer: {optionC}')
            elif optionC == 'Scissors':
                  print(f'<! COMPUTER WINS !>\n'
                        f'=> User: {optionU}\n'
                        f'=> Computer: {optionC}')
            else:
                  print('<! INVALID PLAY !>')
      elif optionU == 'Scissors': # USUÁRIO JOGOU TESOURA
            if optionC == 'Rock':
                  print(f'<! COMPUTER WINS !>\n'
                        f'=> User: {optionU}\n'
                        f'=> Computer: {optionC}')
            elif optionC == 'Paper':
                  print(f'<! USER WINS !>\n'
                        f'=> User: {optionU}\n'
                        f'=> Computer: {optionC}')
            else:
                  print('<! INVALID PLAY !>')
      else:
            print('<! INVALID PLAY !>')
      print('================')
      print('=> Choose another option (choose an ivalid one to quit the app):\n'
            '     [0] Rock\n'
            '     [1] Paper\n'
            '     [2] Scissors\n'
            '     [Others numbers] Exit')
      option = int(input('=> '))
      
      os.system('cls' if os.name == 'nt' else 'clear')