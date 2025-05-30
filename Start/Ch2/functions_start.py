# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def hello_func():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

#hello_func()

# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("ciao");

# function that returns a value
def cube(x):
  return x*x*x

# resulr=cube(3)
# print(resulr)

# function with default value for an parameter
def hello_func(greeting, name=None):
   print("hello world!")
   if (name==None):
     name = input("What is your name? ")
   print(greeting, name)
#hello_func("Ciao", "Marco")
#hello_func("Ciao")
#hello_func(name= "Marco", greeting="ciaoooo")

# function with variable number of parameters
def multi_add(start, *args):
  result=start
  for x in args:
    result = result + x
  return result

print(multi_add(10, 1, 2, 3))


