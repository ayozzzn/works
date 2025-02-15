# JSON in Python.
# Import the json module :
import json

# Parse JSON - Convert from JSON to Python.
# If you have a JSON string, you can parse it by using the json.loads() method.
# Convert from JSON to Python :
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"]) # # the result is a Python dictionary.

# Convert from Python to JSON.
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# Convert from Python to JSON :
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
print(y) # # the result is a JSON string.

# Convert Python objects into JSON strings, and print the values :
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Convert a Python object containing all the legal data types :
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

# Format the Result.
# The json.dumps() method has parameters to make it easier to read the result :
json.dumps(x, indent=4)

# Use the separators parameter to change the default separator :
json.dumps(x, indent=4, separators=(". ", " = "))

# Order the Result.
# Use the sort_keys parameter to specify if the result should be sorted or not :
json.dumps(x, indent=4, sort_keys=True)

