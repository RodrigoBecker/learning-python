"""
Struct conditional (if / else / elif)
"""

age = 30

if age <= 18:
    print("-" * 40)
    print("age is not permited ")

elif age <= 20:
    print("-" * 40) 
    print("age is permited")

else:
    print("-" * 40) 
    print("age is very old!")
