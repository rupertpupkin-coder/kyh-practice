# 39.1

def maximum(a, b, c):
    result = a
    if result < b:
        result = b
    if result < c:
        result = c
    return result


ls = maximum(1, 100, 40)
print(ls)


# 39.2

def add(addList):
    result = 0
    for i in addList:
        result += i
    return result


d = add([100, 2212, 30])
print(d)


# 39.3

def multiply(a):
    result = 1
    for i in a:
        result *= i
    return result

f = multiply([1, 2, 3])
print(f)

