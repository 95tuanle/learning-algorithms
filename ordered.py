items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binary_search(item, item_list):
    listsize = len(item_list) - 1
    lower_idx = 0
    upper_idx = listsize

    while lower_idx <= upper_idx:
        mid_pt = (lower_idx + upper_idx) // 2

        if item_list[mid_pt] == item:
            return mid_pt

        if item > item_list[mid_pt]:
            lower_idx = mid_pt + 1
        else:
            upper_idx = mid_pt - 1

    if lower_idx > upper_idx:
        return None


print(binary_search(23, items))
print(binary_search(87, items))
print(binary_search(250, items))
