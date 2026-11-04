Variable Assignment & Swapping
Assign and swap multiple variables on a single line.

x, y = 10, 20

x, y = y, x  - x becomes 20, y becomes 10

Higher-Order Functions
Pass functions as arguments to other functions.

def apply_twice(func, arg):
    return func(func(arg))

help(abs)
help(print)

print(1, 2, 3, sep=" > ", end="!\n")  # 1 > 2 > 3!

Boolean Truthiness & Logical Operators

# Falsy values: 0, "", [], {}, None
# Truthy values: Non-zero numbers, non-empty collections

is_active = True
has_items = bool([1, 2])  # True

if is_active and has_items:
    print("Ready to process")


items = []

val = items and items[0]  # Evaluates to [] without raising IndexError


Ternary Conditional Expression

score = 85
result = "Pass" if score >= 70 else "Fail"  # "Pass"


List Indexing & Slicing

nums = [10, 20, 30, 40, 50]

print(nums[1:4])     
print(nums[:3])      
print(nums[::2])     

last_item = nums[-1]  # 50
reversed_list = nums[::-1]  # [50, 40, 30, 20, 10]


List Mutation & Search Methods
Modify, extend, and search elements within lists


point = (10, 20)
x, y = point  # x=10, y=20

Dictionary Operations & Lookup
Store and look up key-value pairs in dictionaries.

user = {"name": "Alice", "role": "Data Scientist"}

print(user.keys())    # dict_keys(['name', 'role'])
print(user.values())  # dict_values(['Alice', 'Data Scientist'])


Safe Dictionary Access with `.get()`
counts = {"apples": 5}

# Returns default value if key doesn't exist instead of raising KeyError
oranges = counts.get("oranges", 0)  # 0


 Dictionary Comprehensions
Create transformed dictionaries cleanly in a single line.
python
words = ["apple", "banana"]
word_lengths = {w: len(w) for w in words}  # {'apple': 5, 'banana': 6}
