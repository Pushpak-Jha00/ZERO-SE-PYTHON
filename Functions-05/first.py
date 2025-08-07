# functions 

def calculate(a,b):
  sum = a+b
  print(sum)

calculate(2,4)


def even(a):
  for i in range(a):
    if i % 2 != 0:
      print(i ,"is Even")
  
even(10)


def printCount(a):
  for i in range(1 , a+1):
    print(i);


printCount(10)


def usingWhileLoop(a):
  i = 1
  while a > 0:
    print(i)
    i += 1
    a -= 1

usingWhileLoop(10)