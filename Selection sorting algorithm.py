import random

n = int(input(":"))
zufalliges_my_array = []
for i in range(0, n):
    zufalliges_my_array.append(random.randint(0, n))

print(zufalliges_my_array)


def Sortieren_mit_auswahl(my_array):
    for i in range(len(my_array)):
        minimaler_indexwert = i
        for j in range(i+1, len(my_array)):
            if my_array[j] < my_array[minimaler_indexwert]:
                minimaler_indexwert = j
        my_array[i], my_array[minimaler_indexwert] = my_array[minimaler_indexwert], my_array[i]

Sortieren_mit_auswahl(zufalliges_my_array)

print(zufalliges_my_array)
