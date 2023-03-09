qCandys = int(input('=> How many candys do you have? '))
qPeople = int(input('=> How many people do you have? '))
print('------------------')

dCandys = qCandys // qPeople
lCandys = qCandys % qPeople

print(f'=> Candys per person: {dCandys}\n'
      f'=> Left candys: {lCandys}')