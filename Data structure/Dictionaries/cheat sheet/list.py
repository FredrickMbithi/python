# List comprehensions (use these ALL THE TIME)
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Nested comprehensions (for 2D data)
matrix = [[i*j for j in range(5)] for i in range(5)]

# Slicing tricks
lst = [1, 2, 3, 4, 5]
lst[::-1]    # Reverse
lst[::2]     # Every other element
lst[1:-1]    # Everything except first and last