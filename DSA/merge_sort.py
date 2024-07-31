def merge_sorted(a, b, key, array):
    i = j = k = 0

    while i < len(a) and j < len(b):
        if a[i][key] <= b[j][key]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1
        k += 1
    
    while i < len(a):
        array[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        array[k] = b[j]
        j += 1
        k += 1

def merge_sort(arr, key):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key)
    merge_sort(right, key)
    merge_sorted(left, right, key, arr)

def merge(arr, key, descending=False):
    merged = []
    merge_sort(arr, key)
    if descending:
        while len(arr) != 0:
            merged.append(arr.pop())

    else:
        merged.extend(arr)

    return merged


array = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
array = merge(array, 'time_hours',True)
print(array)
