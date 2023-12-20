def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

# Зчитуємо введене користувачем число
n = int(input("Введіть ціле число n для знаходження n-го числа Фібоначчі: "))

# Визначаємо та виводимо n-е число Фібоначчі
result = fibonacci(n)
print(f"{n}-е число Фібоначчі: {result}")
