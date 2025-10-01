# Creating lists
#numbers  = [1, 2, 3, 4, 5]
#mixed = [1,"hello", 3.14, True]

#Common operations
#numbers.append(6)       #Add to end
#numbers.insert(0, 0)    #insert at index
#numbers.remove(3)       #Remove first occurence
#numbers.pop()           #Remove and return last
#numbers.extend([7, 8, 9])   #Add multiple items
#print(numbers)

numbers = [1, 2, 3, 4, 5]   # define the list

# Accessing
#first = numbers[0]          # first element (index 0) → 1
#last = numbers[-1]          # last element → 5
#slice = numbers[1:4]        # elements from index 1 up to (but not including) 4 → [2, 3, 4]

#print("numbers:", numbers)
#print("first:", first)
#print("last:", last)
#print("slice:", slice)

#List methods
numbers = [1, 2, 3, 4, 5, 6, 7]
#numbers.sort()      #Sort in place
#numbers.reverse()  # Reverse in place
#count = numbers.count(3)    # Count occurrences
#index = numbers.index(5)    # Find index
#print(index)

# List comprehension (powerful!)
#squares = [x**2 for x in range(10)]
#print(squares)
evens = [x for x in range(20) if x % 2 == 0]
print(evens)