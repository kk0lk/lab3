"""

Задача №2

За введеним користувачем цілим числом n визначте n-е число Фібоначчі.

Виконала: Гриб Наталія Григорівна, 31І група
"""

def fibonacci(n):
    if n <=1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b

#Зчитуємо введене користувачем число
n = int(input("Введіть ціле число n для знаходження n-го числа фібоначчі:"))

#Визначаємо та виводимо n-e число фібоначчі
result = fibonacci(n)
print(f"{n}-e число фібоначчі: {result}")
