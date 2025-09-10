N = int(input("Введите N: "))

sequence = []
current = 1

while len(sequence) < N:
    for _ in range(current):
        sequence.append(current)
        if len(sequence) == N:
            break
    current += 1

print(*sequence) # Фролов ЛД ИКБО-20-22
