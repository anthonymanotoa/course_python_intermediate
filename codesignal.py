sequence = [1, 2, 3, 7, 5, 4, 6, 7, 8, 2, 3]
increase = [sequence[i] for i in range(len(sequence) - 1) if sequence[i + 1] > sequence[i]]
print(increase)