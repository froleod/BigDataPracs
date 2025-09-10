numbers = []
total_sum = 0

while True:
    num = int(input())
    numbers.append(num)
    total_sum += num

    if total_sum == 0:
        break

sum_of_squares = sum(x ** 2 for x in numbers)
print(sum_of_squares) # Фролов ЛД ИКБО-20-22
