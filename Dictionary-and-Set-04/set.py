# set are unordered collection and it mutable but it's value are unchangeable (immutable)


num = {2,4,3,4,4,3,"hello", "a"} 
# print(num)
# print(type(num))
# print(len(num))


# set ignore duplicate values
val = set()
val.add(1)
val.add(1)
val.add(2)
val.add(33)

# print(val)
# print(len(val))

# val.remove(33)
# print(val)

# num.update(val)
# print(num)


val1 = {1,2,3,4}
val2 = {3,4,5,6}

print(val1.union(val2))
print(val1.intersection(val2))

