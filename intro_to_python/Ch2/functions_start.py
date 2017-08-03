#
# Example file for working with functions
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def func1():
  print "I am a function"

# func1()
# print func1()
# print func1


def func2(arg1, arg2):
    print arg1, arg2

# func2(10, 20)
# print func2(10, 20)

def cube(x):
    print x*x*x

# cube(3)


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# print power(2)
# print power(2, 3)
# print power(x=3, num=2)


def add_multiple (*arg):
    result = 0
    for x in arg:
        result += x
    return result

print add_multiple(1,2,3,4)
