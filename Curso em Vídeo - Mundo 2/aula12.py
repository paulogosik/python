name = str(input('What is your name? '))
names = ['Guilherme', 'Paulo']
if name in names:
    print('=CEO ACCESS=')
elif name != 'Client':
    print('+WORKER ACCESS+')
else:
    name = str(input('What is your name? '))
    print('Welcome to our company!')
print('Have a good day, {}!'.format(name))
