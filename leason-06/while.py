"""
Loop While

"""

# Example 01:

num = 1

while num < 10:
    print("-" * 40)
    print(num)
    num += 1
    
# Example 02:

response = None

while response != "yes":
    response = input("it is retry?")