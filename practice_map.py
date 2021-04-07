list1 = [1, 2, 3, 4, 5]

# Con list comprehension:
squares = [i**2 for i in list1]
print(squares)

# Con map:
squares_map = list(map(lambda i: i**2, list1))
print(squares_map)