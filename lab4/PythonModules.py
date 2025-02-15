# Create a Module.
# To create a module just save the code you want in a file with the file extension .py.
# Now we can use the module we just created, by using the import statement :
import mymodule
mymodule.greeting("Jonathan")

# Variables in Module.
# The module can contain functions, as already described, but also variables of all types.
# Import the module named mymodule, and access the person1 dictionary :
import mymodule
a = mymodule.person1["age"]
print(a)

# Re-naming a Module.
# Create an alias for mymodule called mx :
import mymodule as mx
a = mx.person1["age"]
print(a)

# Built-in Modules.
# Import and use the platform module :
import platform
x = platform.system()
print(x)

# Using the dir() Function.
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function :
import platform
x = dir(platform)
print(x)

# Import From Module.
# You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1
print (person1["age"])