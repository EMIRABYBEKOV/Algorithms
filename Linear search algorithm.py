def linsearch(x, a):
    k = -1
    for i in range(len(a)):
        if a[i] == x:
            k = i
    return k
x = "Ashgabat"
a = ('Bishkek', "Osh", "Tashkent", "Dushanbe", "Namagan", "Fergana", "Ashgabat")
print(linsearch(x, a))
