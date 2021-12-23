
def Multiply(x, y):
    s1 = 0
    s2 = 0
    while x // (2 ** s1) >= 0:
        s1 = s1 + 1 #grosse-x
    while y // (2 ** s2) >= 0:
        s2 = s2 + 1 #grosse-y
    n = max(s1, s2)
    if n == 1:
        print(x * y)
    else:
        d1 = s1 // 2
        d2 = s2 // 2
        if d1 > d2:
            d = d1
        else:
            d = d2
        num11 = x / (2 ** d)
        num12 = x - num11 * (2 ** d)
        num21 = y / (2 ** d)
        num22 = y / (2 ** d)
        P1 = Multiply(num11, num21)
        P2 = Multiply(num12, num22)
        P3 = Multiply(num11 + num12, num21 + num22)
        print(P1 * (2 ** (2 * (n / 2))) + (P3 - P1 - P2) * (2 ** (2 * (n / 2))) + P2)


#x = int(input("Введите положительное число: "))
#y = int(input("Введите положительное число: "))
#Multiply(x,y)
def itr(n):
    if n == 0:
        return 1
    elif n >= 1:
        print(itr(n) + (n + 1)**2)


n = int(input("SChreib einen Zahl: "))
itr(n)