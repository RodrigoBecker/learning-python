"""
Input console

"""

# Input Data
print("-" * 50)
print("Whats your name?")
name = input()
# Processing
print("-" * 50)
age = input("How old are you?")
# Exit Data
print("-" * 50)
print("Welcome %s, i am %s years old" % (name, age))  # warnning deprecate method
print("Welcome {0} i am {1}".format(name, age)) # method format
print(f"Welcom {name} i am {int(age)} years old") # method f-string and cast type convert
print(f"{name} born {2021- int(age)}") # operation type int
