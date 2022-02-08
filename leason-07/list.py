# list in python is array / matriz

from math import prod


type([])

# Type of list

list_one = [1, 2, 34, 50, 59, 90]
list_two = ["A", "B", "C", "D", "E", "F", "G"]
list_three = []  # output list
list_four = list(range(11))  # output [0,1,2,3,4,5,6,7,8,9,10]
list_five = list("geek universy")  # output ["g", "e", "e", "k", "u", "n", "i", "v", "e", "r", "s", "y"]
list_one.reverse()  # output [90, 59,50,34,2,1]

# use slicing:
print(list_one[::-1])  # reverse list with slicing
print(list_two[::-1])

# copy list:

list_copy = list_one.copy()

# length list:
print(len(list_four))

# remove last element in list:

list_one.pop()  # output [1,2,34,50,59]
# obs: pop return value removed in list

# remove element with index array:
list_one.pop(3)  # output [1,2,34,59,90]


# remove all elements the list:
list_one.clear()  # output []

# operation with array:
list_new = list_one * 3  # output [1, 2, 34, 50, 59, 90, 1, 2, 34, 50, 59, 90, 1, 2, 34, 50, 59, 90]

# easy convert string to type list:
str_value = "geek universy"
str_to_list = str_value.split()  # output ["geek", "universy"]


# concat string array:

str_array = ["god", "geek", "university"]

new_string = "-".join(str_array)
print(new_string)

# merge types formats in list:

list_merge_type = ["A", 1, "G", "3440", "geek"]
print(list_merge_type)

# interation in list in loop for:

list_numb = [1, 2, 4]

soma = 0
for x in list_numb:
    soma += x
    print(x)
print(soma)

# interation in list with while:

product = None
cart = []

while product != "exit":
    product = input("Add item in cart: ")
    cart.append(product)

print(cart)

# add index in list with enumarate

colors = ["green", "red", "white", "gray"]
for index, color in enumerate(colors):
    print(index, color)

# other methods in list:

# -> Find index in list:
numbers = [1, 2, 3, 4, 5]
print(numbers.index(3))


# search element in range:

print(numbers.index(4, 1, 5))

# search max and min

list_numbers = [1, 2, 3, 4, 5]
print(sum(list_numbers))  # output 15
print(max(list_numbers))  # output 5
print(min(list_numbers))  # output 1
print(len(list_numbers))  # output 5

# convert list to tuple:

typing_list = [1, 2, 4]
convert_tuple = tuple(typing_list)
print(convert_tuple)
print(type(convert_tuple))

# extract value list:

list_extract = [2, 4, 56]
value_1, value_2, value_3 = list_extract
print(value_1)
print(value_2)
print(value_3)


# copy list to list (Shallow copy / deep copy)

list_to_copy = [1, 3, 4, 5]
new_list_copied = list_to_copy.copy()
new_list_copied.append(0)
print(new_list_copied)  # output [1,3,4,5] - deep copy
print(list_to_copy)  # output [1,3, 4, 5]
# ---------------------------------------------------#

list_old_shallow_copy = [1, 4, 6, 9, 0]
list_shallwow_copied = list_old_shallow_copy

list_shallwow_copied.append(49)
print(list_old_shallow_copy)  # output [1, 4, 6, 9, 0, 49]
print(list_shallwow_copied)  # output [1, 4, 6, 9, 0, 49]
