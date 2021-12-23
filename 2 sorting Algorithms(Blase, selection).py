import time
import random


n = int(input(":"))
zufalliges_my_array = []
zufalliges_my_array1 = []
for i in range(n - 1):
   x = random.randint(1, 1000)
   zufalliges_my_array.append(x)
   zufalliges_my_array1.append(x)

print(zufalliges_my_array)


def Sortieren_mit_auswahl(my_array):
    for i in range(len(my_array)):
        minimaler_indexwert = i
        for j in range(i+1, len(my_array)):
            if my_array[j] < my_array[minimaler_indexwert]:
                minimaler_indexwert = j
        my_array[i], my_array[minimaler_indexwert] = my_array[minimaler_indexwert], my_array[i]

def Blase_Sortierung(my_array):
    ausgetauscht = True
    while ausgetauscht:
        ausgetauscht = False
        for i in range(len(my_array) - 1):
            if my_array[i] > my_array[i + 1]:
                my_array[i], my_array[i + 1] = my_array[i + 1], my_array[i]
                ausgetauscht = True

start_time = time.time()
Sortieren_mit_auswahl(zufalliges_my_array)
print("Sortieren mit auswahl",zufalliges_my_array)
print("--- %s seconds ---" % (time.time() - start_time))

b = time.time()
Blase_Sortierung(zufalliges_my_array1)
print("Blase_sortierung", zufalliges_my_array)
print("--- %s seconds ---" % (time.time() - b))

def itr(n):
    if n == 1:
        print(1/2)
    elif n > 1:
        g = n
        print(itr(g)+(n+1)**2)

n = int(input("SChreib einen Zahl: "))
itr(n)
