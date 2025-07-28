marks = [45,67,89,46,667,667,"Hello", "Hum", "Vinodh"]
print(marks)
print(type(marks))
print(len(marks))
print(marks[4])
print(marks[8])

marks[4] = 67
print(marks)


# list slicing
data = [1,2,3,"a","v","f",4,5,6]
print(data[0:4])
print(data[3:6])
print(data[3:])
print(data[:3])


# List Methods
data2 = [2,1,5]


data2.insert(2,3)
print(data2)

data2.remove(3)
print(data2)

data2.pop(1)
print(data2)

data2.append(3)
print(data2)

data2.reverse()
print(data2)

data2.sort()
print(data2)

data2.append(4)
data2.sort()
print(data2)

data2.sort(reverse=True)
print(data2)