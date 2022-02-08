# maps in python is dict

amount = {"january": 100, "february": 240, "march": 400}


for value in amount:
    print(f"{value} : {amount[value]}")
    print("-" * 40)

print(amount.keys())  # output dict_keys(['january', 'february', 'march'])

# method .keys()

for value in amount.keys():
    print(amount[value])

print(amount.values())  # dict_values([100, 240, 400])

# access value in dict

for value in amount.values():
    print(value)

# extract value in dict:

for key, value in amount.items():
    print(f"key: {key} value: {value}")


print(sum(amount.values()))
print(max(amount.values()))
print(min(amount.values()))
print(len(amount))