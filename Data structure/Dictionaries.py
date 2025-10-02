# Creating dictionaries
person = {
    "name":"Alice",
    "age":25,
    "city": "Nairobi"
}
# Accesing
name = person["name"]
age = person.get("age")
city = person.get("country", "Kenya")

#adding/updating
person["email"] = "alice@example.com"
person.update({"phone": "123456"})

#Removing
del person["city"]
email =  person.pop("email")

#Iterating
for kei in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}