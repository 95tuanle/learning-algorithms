items = ["apple", "pear", "orange", "banana", "apple", "orange", "apple", "pear", "banana", "orange", "apple", "kiwi",
         "pear", "apple", "orange"]

filter_dict = dict()

for item in items:
    filter_dict[item] = 0

result = set(filter_dict.keys())
print(result)
