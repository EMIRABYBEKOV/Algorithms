M = int(input("Введите натуральное число \n"))
N = M + 2
A = []
for i in range(N):
    A.append(i)       
for i in range(N):
    if i != 0 and i != 1 and A[i] != 0:
        m = i + i
        while m <= M:
            A[m] = 0
            m = m + 1
print("Список простых чисел, не привышающих заданное число:")
for i in range(N):
    if i >= 2 and A[i] != 0:
        print(A[i])
