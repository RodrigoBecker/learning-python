"""
Loop for

"""

result = [1,2,2,3,4]

# Example 01 - for:

for item in result:
    print("-"* 40)
    print(item)

# Example 02 - for range:

for number in range(1,10):
    print("-"* 40)
    print(number)
    
    
# Example 03 - for enumerate:

for i, v in enumerate(result):
    print(i, v)


# Example 04 - descart value index:

for _, v in enumerate(result):
    print("-"* 40)
    print(v)

# Example 05 with unicode caractecter:

input_number = int(input("Insert number"))

for n in range (1, input_number +1):
    print("-"* 40)
    print(n)
    print("\U0001F60D")
