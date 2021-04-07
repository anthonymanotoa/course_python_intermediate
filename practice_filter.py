# Usando list comprehension:
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd_comprehension = [i for i in my_list if i % 2 != 0]
print(odd_comprehension)

# Usando filter:
odd_filter = list(filter(lambda i: i % 2 != 0, my_list))
print(odd_filter)