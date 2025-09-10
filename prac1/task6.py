A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']

result = {}

for i in range(len(A)):
    letter = B[i]
    number = A[i]
    result[letter] = result.get(letter, 0) + number

print(result) # Фролов ЛД ИКБО-20-22