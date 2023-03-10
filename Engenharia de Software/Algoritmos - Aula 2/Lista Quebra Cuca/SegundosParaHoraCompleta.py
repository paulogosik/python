sec = int(input('=> How many seconds is it? '))
print('----------------')

hours = sec // 3600
fMin = sec % 3600

min = fMin // 60
fSec = fMin % 60

print(f'=> Hours: {hours} hour(s)\n'
      f'=> Minutes: {min} minute(s)\n'
      f'=> Seconds: {fSec} second(s)')