name = input('=> What is your name? ')
height = float(input('=> What is your height in meters? '))
weight = float(input('=> What is your weight in kg? '))
print('---------')

imc =  weight / (height * height)

if imc < 18.5:
    print(f'=> {name}, your IMC is: {imc:.2f}, so, you are =UNDERWEIGHT=')
elif imc >= 18.5 and imc < 25:
    print(f'=> {name}, your IMC is: {imc:.2f}, so, you are on your =NORMAL WEIGHT=')
elif imc >= 25 and imc < 30:
    print(f'=> {name}, your IMC is: {imc:.2f}, so, you are =OVERWEIGHT=')
elif imc >= 30 and imc < 40:
    print(f'=> {name}, your IMC is: {imc:.2f}, so, you have =OBESITY=')
else:
    print(f'=> {name}, your IMC is: {imc:.2f}, so, you have =MORBID OBESITY=')