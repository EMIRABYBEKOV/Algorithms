A = float(input('Введите значение числа А\n'))
Eps = float(input('Введите  значение абсолютной ошибки\n'))
X0 = A/2.0
X1 = A
counter = 0

while abs(X1 - X0) >= Eps:
    X0 = X1
    X1 = 0.5 * (X0 + A/X0)
    counter += 1

print("Абсолютная точность значения")
print(Eps)
print("Квадратный корень из заданного числа")
print(X1)
print("Число итарций в алгоритме")
print(counter)
