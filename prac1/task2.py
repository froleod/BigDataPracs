import math

def main():
    figures = {}
    print("Введите фигуры и их параметры. Для завершения ввода оставьте название пустым.")

    while True:
        figure = input("Название фигуры (треугольник, прямоугольник, круг): ").strip().lower()
        if not figure:
            break

        if figure == "треугольник":
            a = float(input("Сторона a: "))
            b = float(input("Сторона b: "))
            c = float(input("Сторона c: "))
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                figures[figure] = area
            else:
                print("Ошибка: треугольник с такими сторонами не существует.")

        elif figure == "прямоугольник":
            length = float(input("Длина: "))
            width = float(input("Ширина: "))
            figures[figure] = length * width

        elif figure == "круг":
            radius = float(input("Радиус: "))
            if radius >= 0:
                figures[figure] = math.pi * radius ** 2
            else:
                print("Ошибка: радиус не может быть отрицательным.")
        else:
            print("Неизвестная фигура. Доступные: треугольник, прямоугольник, круг.")

    print("\nПлощади фигур:")
    for fig, area in figures.items():
        print(f"{fig}: {area:.2f}")

    return figures # Фролов Л.Д. ИКБО-20-22

result = main()