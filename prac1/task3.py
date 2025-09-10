def calculator(a, b, operation):

    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '/':
        if b == 0:
            return "Ошибка: деление на ноль"
        result = a / b
    elif operation == '//':
        if b == 0:
            return "Ошибка: деление на ноль"
        result = a // b
    elif operation == 'abs_a':
        result = abs(a)
    elif operation == 'abs_b':
        result = abs(b)
    elif operation == 'pow' or operation == '**':
        result = a ** b
    else:
        return "Ошибка: неизвестная операция"

    return result


try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Введите операцию (+, -, /, //, abs_a, abs_b, pow, **): ")

    result = calculator(a, b, operation)
    print("Результат:", result)
except ValueError:
    print("Ошибка: введите корректные числа") # Фролов ЛД ИКБО-20-22