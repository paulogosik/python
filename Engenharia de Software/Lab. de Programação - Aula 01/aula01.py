# EXEMPLO 01 ---------------------------------------------------
# def RetornaA():
#     a = 5
#     print(f"'a' dentro do método: {a}")
#     #return a

# print(RetornaA)

# EXEMPLO 02 ---------------------------------------------------
# def f(x, y):
#     x = x + 1
#     y.append(4)

# x = 1
# y = [1, 2 , 3]

# print(f"X: {x}")
# print(f"Y: {y}")

# f(x, y)

# print(f"X: {x}")
# print(f"Y: {y}")

# EXEMPLO 03 ---------------------------------------------------
# def f():
#     a = 5
#     print(f"'A' dentro do método {a}")
#     return a

# a = 3
# print(F"A: {a}")
# a = f()
# print(F"A: {a}")

# EXEMPLO 04 ---------------------------------------------------
a = 30
print(f"=> A: {a}")

def FuncaoA():
    global a
    a = 5
    print(f"=> A da função: {a}")
    return a

a = 3
print(f"=> A antes de chamar a função: {a}")
print(FuncaoA())
print(f"=> A depois de chamar a função: {a}")