"""
Exit loop with break
"""

# Example 01:

for num in range(1, 10):
    if num == 6:
        break
    else:
        print(num)
print("exit loop")

# Example 02:

while True:
    comand = input("Press yes to Exit!")
    if comand == "yes":
        break