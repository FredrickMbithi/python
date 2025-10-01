# String operations
text = "Hello World"
print(text.lower())      # hello world
print(text.upper())      # HELLO WORLD
print(text.split())      # ['Hello', 'World']
print(len(text))         # 11

# String formatting
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age}")
print("My name is {} and I'm {}".format(name, age))

# String slicing
print(text[0:5])         # Hello
print(text[:5])          # Hello
print(text[6:])          # World
print(text[-5:])         # World (from end)