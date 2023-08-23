items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_max(input_items):
    max_input = input_items[0]
    for item in input_items:
        if item > max_input:
            max_input = item
    return max_input


print(find_max(items))
