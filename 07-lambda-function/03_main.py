# Add Two Numbers

add = lambda a,b: a+b
print("Add two numbers: ",add(2,3))

# Basic Example - Double a Number 

double = lambda x: x*2
print("Double a number: ",double(2))

#Conditional Example - Even or Odd

even_or_odd = lambda x: "Even" if x%2 == 0 else "Odd"
print("Number is: ",even_or_odd(5))

#Sorting with Lambda

words = ["banana","apple", "banana", "cherry", "date"]
sort_words = sorted(words, key=lambda word: word[0])
print(sort_words)


#Using map() with Lambda - Double Numbers 

nums = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, nums))
print(doubled)