#Default arguments
##Define a function by assigning default values
def greet(name,message="Hello"):
    print(f"{message},{name}!")
#Calling The Function With Only The Required arugument
greet("Bob")
#Overridding the default argument
greet("Alice","Hi")
