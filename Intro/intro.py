import sys

#to run the program u must do this boring staff python intro.py
# the coments with this thing #

print("Hello World");

# Checking the Python version
print(sys.version);


"""  multilines comment!

# trying if conditions with allowed ways
if (2 > 0):print("Woow true!")
if (2 > 0): print("Woow true!")
if 2 > 0:
    print("Woow true!");

"""


""" using variables and specifying the data type and getting the data type
x = 5
y = "John"
print(x)
print(y)

print(type(y),"                   ", type(x))


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


print(x)
print(y)
print(z)

"""





"""    Many Values to Multiple Variables


x, y, z = "Orange", "Banana", "Cherry"
print("-------")
print(x)
print(y)
print(z)
print("-------")

x = y = z = "Orange"
print(x)
print(y)
print(z)
print("-------")

x, y, z = ["apple", "banana", "cherry"] #unpacking
print(x)
print(y)
print(z)
print("=> ", x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
"""



"""    #functions

def my_function():
  print("Hello from a function")

def my_function_with_params(fname):
  print("Hello from a function that call: " +  fname)

def my_function_args(*args):
  print("my args that have index number 2 is: " + args[2])
  for x in args:
    print("args : " + x)


my_function()
my_function_with_params("youssef")
my_function_args("one", "two", "three")

"""