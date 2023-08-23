items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_max(input_items):
    # max_input = input_items[0]
    # for item in input_items:
    #     if item > max_input:
    #         max_input = item
    # return max_input

    if len(input_items) == 1:
        return input_items[0]
    op1 = input_items[0]
    op2 = find_max(input_items[1:])
    if op1 > op2:
        return op1
    else:
        return op2


print(find_max(items))
