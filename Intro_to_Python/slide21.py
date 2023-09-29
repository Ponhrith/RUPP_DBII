fruits = ["apple","banana"]
fruits.append("cherry")
print(fruits)

fruits = ["apple","banana"]
fruits.insert(1,"cherry")
print(fruits)

fruits = ["apple","banana","banana","cherry"]
fruits.remove("banana")
print(fruits)

removed_fruit = fruits.pop(1)
print(removed_fruit)
print(fruits)