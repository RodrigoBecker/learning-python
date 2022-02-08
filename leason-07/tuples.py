# tuples

# every change tuple always create new tuple

tuple_example = (1, 3, 5)  # output type is tuple
print(type(tuple_example))
tuple_example_2 = 1, 3, 5  # output type is tuple
print(type(tuple_example_2))

tuple_example_3 = 4  # output type is int. NO is tuple
print(type(tuple_example_3))

tuple_example_4 = (4,)  # output type is tuple
print(tuple_example_4)

tuple_range = tuple(range(11))
print(tuple_range)

# extract value in tuple

tuple_example_5 = ("geek", "universy")
value_1, value_2 = tuple_example_5
print(value_1)
print(value_2)

# methods for tuples:

tuple_example_6 = (1, 3, 5, 6)
print(sum(tuple_example_6))
print(max(tuple_example_6))
print(min(tuple_example_6))
print(len(tuple_example_6))


# concat tuple:

tuple_values_1 = (1, 2, 4)
tuple_values_2 = (5, 6, 7)
concat_tuple = tuple_values_1 + tuple_values_2
print(concat_tuple)

# OBS: tuples is imutable! but we can overload your values

# iteration in tuples:


tuple_values = (1, 2, 5)
for value in tuple_values:
    print(value)

for index, value in enumerate(tuple_values):
    print(index, value)

# count elements in tuple:

length_tuple = ("a", "d", "n", "i", "a")
print(length_tuple.count("a"))

# convert string to tuple:

string_value = "geek"
convert_tuple = tuple(string_value)
print(convert_tuple)

# access elements

month = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "Agust",
    "September",
    "October",
    "November",
    "December",
)

print(month[5])  # output June
print(month[3])  # output April

for m in month:
    print("-" * 50)
    print(m)

# slicing in tuple:

print(
    month[::1]
)  # output ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agust', 'September', 'October', 'November', 'December')
print(month[1:5])  # output ('February', 'March', 'April', 'May')
print(
    month[::-1]
)  # output ('December', 'November', 'October', 'September', 'Agust', 'July', 'June', 'May', 'April', 'March', 'February', 'Janua

# OBS: 

"""
-> tuple is very fast than list 
-> tuple are imutables, bring more securtity for your code
"""