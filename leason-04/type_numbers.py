"""
Type number

"""

# example:
num_a = 10
num_b = 5
 
print("-" * 40)
print("sum")
RESULT = num_a + num_b
print(RESULT)

print("-" * 40)
print("subtraction")
RESULT = num_a - num_b
print(RESULT)

print("-" * 40)
print("multiplation")
RESULT = num_a * num_b
print(RESULT)

print("-" * 40)
print("division")
RESULT = num_a / num_b
print(RESULT)

print("-" * 40)
print("division not exactly")
RESULT = num_a // num_b
print(RESULT)

print("-" * 40)
print("module operation")
RESULT = num_a % num_b
print(RESULT)

print("-" * 40)
print("exponentiation")
RESULT = num_a ** num_b
print(RESULT)

# Example separation decimal places:
print(1_000_000_00)


# Example increment:
num_a += 1
print(num_a)

num_a -= 1
print(num_a)


num_a *= 1
print(num_a)

num_a /= 1
print(num_a)


# Example function built in type 

print(type(num_b))

print(dir(num_b))