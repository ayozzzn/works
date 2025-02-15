# Built-in Math Functions.
# The min() and max() functions can be used to find the lowest or highest value in an iterable :
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x) # 5.
print(y) # 25.

# The abs() function returns the absolute (positive) value of the specified number :
x = abs(-7.25)
print(x) # 7,25.

# The pow(x, y) function returns the value of x to the power of y (xy) :
x = pow(4, 3)
print(x) # 64.

# The Math Module.
# To use it, you must import the math module :
import math

# The math.sqrt() method for example, returns the square root of a number :
import math
x = math.sqrt(64)
print(x) # 8.0.

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result :
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # 2.
print(y) # 1.

# The math.pi constant, returns the value of PI :
import math
x = math.pi
print(x) # 3.141592653589793.
