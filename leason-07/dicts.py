# dict is element (key and value {})

print(type({}))  # output type is dict

example_dict = {"key": "value_1", "key2": "value_2", "key_3": "value_3"}

example_dict_two = {"BR": "Brazil", "EUA": "USA"}
example_dict_three = dict(BR="Brazil", EUA="USA")

# Access Element in dict:

example_dict_four = {"Model1": "value1", "Model2": "value2"}

print(example_dict_four["Model1"])  # output "value1"
print(example_dict_four.get("Model2"))  # output "value2
print(example_dict_four.get("Model3"))  # output None (NoneType)

# example validation value in dict:
is_found = example_dict_four.get("Model1")

if is_found:
    print("I found value!!")
else:
    print("Not found value")

verification = example_dict_four.get("Model3", "Not found")
print(verification)  # output Not found

# search key is in dict:

print("Model1" in example_dict_four)  # output is True
print("Model3" in example_dict_four)  # output is False

# tuple is in dicts:

example_dict_tuple = {(35.7893, 39.6917), "Tókio", (40.7189, 75.904), "New York", (37.900, 122.909), "São Paulo"}
print(example_dict_tuple)

# insert element in dict:

received_amount = {"january": 200.0, "february": 490.0, "march": 500.0}
received_amount["april"] = 600.0
print(received_amount)

new_item = {"may": 800.0}
received_amount.update(new_item)  # received_amount.update({"may": "800.0"})


# change value element in dict:

received_amount.update({"may": 900.0})
received_amount.update({"june": 100.0})
print(received_amount)

# OBS dict is not repeat key !!!


# Removed item is in dict:
received_amount.pop("january")  # output {'february': 490.0, 'march': 500.0, 'april': 600.0, 'may': 900.0}
print(received_amount)
print(received_amount)  # output {'february': 490.0, 'march': 500.0, 'april': 600.0, 'may': 900.0, 'june': 100.0}

del received_amount["february"]  # output {'march': 500.0, 'april': 600.0, 'may': 900.0, 'june': 100.0}
print(received_amount)

# manipulation collection (list / dict / tuple)

cart = []
product_one = ["Playstation 4", 1, 2400.09]
produtct_two = ["God of War", 1, 59.00]

cart.append(product_one)
cart.append(produtct_two)

print(cart)

product_one_tuple = ("Playstation 4", 1, 2400.09)
product_two_tuple = ("God of War", 1, 59.00)
cart_tuple = (product_one_tuple, product_two_tuple)
print(cart_tuple)

cart_dict = []

product_one_dict = {"name": "Playstation 4", "unit": 1, "value": 2400.09}
product_two_dict = {"name": "God of Wa", "unit": 1, "value": 59.00}
cart_dict.append(product_one_dict)
cart_dict.append(product_two_dict)
print(cart_dict)

# methods dict:

example_dict_7 = {"a": 1, "b": 2, "c": 4}

example_dict_7.clear()  # output {}
print(example_dict_7)

example_dict_8 = {"a": 1, "b": 2, "c": 4}
new_dict_copy = example_dict_8.copy()
new_dict_copy["d"] = 9
print(new_dict_copy)  # output  {"a": 1, "b": 2, "c": 4, "d": 9}
print(example_dict_8)  # output  {"a": 1, "b": 2, "c": 4}

new_dict_shallow_copy = example_dict_8
new_dict_shallow_copy["e"] = 10
print(new_dict_shallow_copy)  # output {"a": 1, "b": 2, "c": 4, "e": 10}
print(example_dict_8)  # output {"a": 1, "b": 2, "c": 4, "e": 10}
print(example_dict_8)  # output {"a": 1, "b": 2, "c": 4, "e": 10}

# Other create new dict:

other_dict = {}.fromkeys("a", "b")
print(other_dict)
user = {}.fromkeys(
    ["name", "point", "mail", "profile"], "unknow"
)  # output {'name': 'unknow', 'point': 'unknow', 'mail': 'unknow', 'profile': 'unknow'}
print(user)
new_user = {}.fromkeys("name", "value")  # output {'n': 'value', 'a': 'value', 'm': 'value', 'e': 'value'}
print(new_user)

new_user_range = {}.fromkeys(range(1, 11), "value")
print(
    new_user_range
)  # output {1: 'value', 2: 'value', 3: 'value', 4: 'value', 5: 'value', 6: 'value', 7: 'value', 8: 'value', 9: 'value', 10: 'value'}
