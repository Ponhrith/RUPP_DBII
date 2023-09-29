person = {"name": "Alice", "age":25 , "city": "New York"}
print(person["name"])
print(person["age"])

person = {"name": "Alice", "age":25 , "city": "New York"}
person["age"] = 26
print(person)

person = {"name": "Alice", "age":25 , "city": "New York"}
person["gender"] = "Female"
print(person)

person = {"name": "Alice", "age":25 , "city": "New York"}
del person["age"]
print(person)

# age = person.pop("age")
# print(age)
# print(person)