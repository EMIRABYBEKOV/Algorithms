FibArray =[0,1]

def fibonacci(n):
    if n < 0:
        print("Некорректный ввод индекса элемента числовой последовательности")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        zeitlich_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(zeitlich_fib)
        return zeitlich_fib

import time
t1 = time.clock()

Zahl = 1000

for i in range(Zahl + 1):
    print(i + 1, fibonacci(i + 1))

t2 = time.clock() - t1
print("Время затраченное для выполнения программ в секундах", t2)



