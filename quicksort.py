items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def quick_sort(dataset, first, last):
    if first < last:
        pivot_idx = partition(dataset, first, last)
        quick_sort(dataset, first, pivot_idx - 1)
        quick_sort(dataset, pivot_idx + 1, last)


def partition(datavalues, first, last):
    pivotvalue = datavalues[first]
    lower = first + 1
    upper = last

    done = False
    while not done:
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp
    return upper


print(items)
quick_sort(items, 0, len(items) - 1)
print(items)
