name = input('=? What is the name of the student? ')
n1 = float(input('=? First grade weighted 1: '))
n2 = float(input('=? Second grade weighted 2: '))
n3 = float(input('=? Third grade weighted 3: '))
print('=========')

p1 = 1
p2 = 2
p3 = 3
m1 = n1 * p1
m2 = n2 * p2
m3 = n3 * p3
mt = (m1 + m2 + m3) / (p1 + p2 + p3)

print(f'Student: {name}\n'
      f'Weighted Average: {mt:.2f}')