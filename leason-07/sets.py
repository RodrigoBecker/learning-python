# sets

# sets is not replied values
# sets is not order items
# sets is not acccess in index value

# sets is represent{}

from operator import ne


example_set = {1, 2, 4, 5, 6, 0, 1}
print(example_set)  # output {1, 2, 4, 5, 6, 0}
print(type(example_set))

example_set_two = set({1, 3, 5, 3})
print(example_set_two)
print(type(example_set_two))


if 3 in example_set_two:
    print("I found value!!")
else:
    print("I not found value!!")

example_list = [1, 4, 45, 33, 67, 98]
print(f"Example List: {example_list}")
example_set_three = {1, 4, 45, 33, 67, 98}
print(f"Example set: {example_set_three}")
example_tuple = (1, 4, 45, 33, 67, 98)
print(f"Example tuple:  {example_tuple}")
example_dict = (example_list, "dict")
print(f"Example dict: {example_dict}")

# all merge typing in set:

example_type_merge_set = {1, 5, 9, 7, True, "A", "D"}
print(example_type_merge_set)

# interation element in set:

for value in example_type_merge_set:
    print("-" * 40)
    print(value)

city = ["SP", "RJ", "PR", "MG", "SP"]
print(len(city))

print(len(set(city)))  # output 4
print(set(city))  # output {'MG', 'RJ', 'SP', 'PR'}


# insert element in set:
s = {1, 2, 4, 5}
s.add(8)
print(s)  # output {1, 2, 4, 5, 8 }

# remove element in set:
s.remove(2)
print(s)  # output {1, 4, 5, 8}

s.discard(5)
print(s)  # output {1, 4, 8}
# OBS method discard is not thow exception when not foud a element

# Copy set for other set

new_set = s.copy()
new_set.add(5)
print(new_set)  # output {8, 1, 4, 5} - deep copy

new_set_copy = new_set
new_set_copy.add(50)
print(new_set)  # output {1, 4, 5, 8, 50}
print(new_set_copy)  # output {1, 4, 5, 8, 50}


# remove all element in set:

new_set.clear()  # output {}


# operation in sets:

python_students = {"Anna", "David", "John", "Michel"}
java_students = {"David", "Michel", "Alfred", "Mia"}

set_union_students = python_students.union(java_students)
print(set_union_students)  # output {'David', 'Alfred', 'Mia', 'John', 'Anna', 'Michel'}

set_intersect_student = python_students.intersection(java_students)
print(set_intersect_student) # output {'David', 'Michel'}

other_mode_intersect = python_students & java_students
print(other_mode_intersect) # output {'David', 'Michel'} 

set_only_java = java_students.difference(python_students)
print(set_only_java) # output {'Alfred', 'Mia'}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))