person = {"name": "Alice", "age":25 , "city": "New York"}
for key in person:
    print(key)

person = {"name": "Alice", "age":25 , "city": "New York"}
for value in person.values():
    print(value)

person = {"name": "Alice", "age":25 , "city": "New York"}
for key, value in person.items():
    print(f'{key}:{value}')