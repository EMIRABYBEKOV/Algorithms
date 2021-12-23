
def binsearch(x, a):
    erste = 0
    letzte = len(a) - 1
    index = -1
    while (erste <= letzte):
        mitte = (erste + letzte) // 2
        if a[mitte] == x:
            index = mitte
            return index
        else:
            if x < a[mitte]:
                letzte = mitte - 1
            else:
                erste = mitte + 1
        print("erste = ", erste, "letzte = ", letzte)
    return index

x = 0
a = [10, 9, 8, 7, 6, 4, 5, 3, 1, 2, 4, 0]
a = sorted(a)
print(binsearch(x, a))



