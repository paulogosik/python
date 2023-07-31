# EXEMPLO 01 ---------------------------------------------------
# def RetornaA():
#     a = 5
#     print(f"'a' dentro do método: {a}")
#     #return a

# print(RetornaA)

# EXEMPLO 02 ---------------------------------------------------
def f(x, y):
    x = x + 1
    y.append(4)

x = 1
y = [1, 2 , 3]

print(f"X: {x}")
print(f"Y: {y}")

f(x, y)

print(f"X: {x}")
print(f"Y: {y}")