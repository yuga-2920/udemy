def exchange(a, b):
    c = a
    a = b
    b = c
    return a, b

def add(a, b):
    sum = []
    if len(a) != len(b):
        print('error')
        exit()
    for (x, y) in zip(a, b):
        sum.append(x + y)
    return sum

