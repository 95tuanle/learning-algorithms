items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted(item_list):
    for i in range(len(item_list) - 1):
        if item_list[i] > item_list[i + 1]:
            return False
    return True


print(is_sorted(items1))
print(is_sorted(items2))
