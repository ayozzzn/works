# Local Scope.
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function :
def myfunc():
  x = 300
  print(x)
myfunc()

# Function Inside Function.
# The local variable can be accessed from a function within the function :
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()

# Global Scope.
# A variable created in the main body of the Python code is a global variable and belongs to the global scope :
x = 300
def myfunc():
  print(x)
myfunc()
print(x)

# Naming Variables.
# The function will print the local x, and then the code will print the global x :
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

# Global Keyword.
# If you use the global keyword, the variable belongs to the global scope :
def myfunc():
  global x
  x = 300
myfunc()
print(x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword :
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)

# Nonlocal Keyword.
# If you use the nonlocal keyword, the variable will belong to the outer function :
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())