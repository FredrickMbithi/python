#def fizzbuzz():
#    for i in range(1, 101):
#        if i % 3 == 0 and i % 5 == 0:
#            print("FizzBuzz")
#        elif i % 3 == 0:
#            print("Fizz")
#        elif i % 5 == 0:
#            print("Buzz")
#        else:
#            print(i)

# Cleaner version:
#def fizzbuzz():
#    for i in range(1, 101):
#        output = ""
#        if i % 3 == 0:
#            output += "Fizz"
#        if i % 5 == 0:
#            output += "Buzz"
#        print(output or i)