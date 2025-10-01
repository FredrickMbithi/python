# my code
#text = "Hello world"
#print(text[::-1])

#claude solution
#def reverse_string(text):
#    return text[::-1]

#print(reverse_string("54321"))

#Method 3: Loop
def reverse_string(text):
    result = ""                     # start with nothing
    for char in text:               # look at each letter in the text
        result = char + result      # put the new letter in FRONT of what you already have 
    return result
print(reverse_string("54321"))