#### Collections Counter #### 

# High-performance Container Datetype
from collections import Counter
from operator import ne

example_item_list = [1 ,2 ,3 ,4, 2, 3, 5, 5, 4, 89, 0, 0]

result_counter = Counter(example_item_list)
print(result_counter) # output Counter({2: 2, 3: 2, 4: 2, 5: 2, 0: 2, 1: 1, 89: 1})
print(Counter("Good of war")) # output Counter({'o': 3, ' ': 2, 'G': 1, 'd': 1, 'f': 1, 'w': 1, 'a': 1, 'r': 1})

text_example = """

Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including 
versions of Lorem Ipsum.

"""

letter = text_example.split()
result_counter_text = Counter(letter)
print(result_counter_text)
print(result_counter_text.most_common(5)) # return the five most letter in text


#-------------------------------------------------------------------------------------------------------------------# 

### Collection Default Dict ###

from collections import defaultdict

dictionary_example = {"title": "lorem ipsum"}
print(dictionary_example) # output {'title': 'lorem ipsum'}
print(dictionary_example["title"]) # output lorem ipsum'

example_dict = defaultdict(lambda: 0)
example_dict["title"] = "lorem ipsum"
print(example_dict)
print(example_dict["other"])
print(example_dict)

#-------------------------------------------------------------------------------------------------------------------#

### Collection Default OrderedDictt ###

from collections import OrderedDict

new_dict = {"a": 1, "b": "2", "c": 3, "d": 4, "e": 5}
print(new_dict)

for key, value in new_dict.items():
    print(f"{key}:{value}")

new_dict_ordered = OrderedDict({"a": 1, "b": "2", "c": 3, "d": 4, "e": 5})

for key , value in new_dict_ordered.items():
    print(f"{key}:{value}")

