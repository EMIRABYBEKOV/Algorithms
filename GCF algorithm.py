def nod1(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return


x = int(input("a = "))
y = int(input("b = "))
print("NOD", nod1(x, y))
