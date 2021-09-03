# ITP Week 1 Day 4 (In-Class) Practice
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()
z = car.items()

# before the change
print(x)
print(y)
car["condition"] = "fair" # new key created
car["year"] = 2018

#after the change
print(x)
print(y)
print(z)