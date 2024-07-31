def binary_search(val,array,left_index,right_index):
    mid_index = int((left_index + right_index) / 2)
    
    if left_index < 0 or left_index > right_index or mid_index >= len(array):
        return None

    if array[mid_index] == val:
        return mid_index

    if array[mid_index] >= val:
        right_index = mid_index - 1
        return binary_search(val,array,left_index,right_index)

    if array[mid_index] <= val:
        left_index = mid_index + 1
        return binary_search(val,array,left_index,right_index)

    return mid_index


def find_all_occurrence(val,array):
    occ = []
    first_occ = binary_search(val,array,0,len(array))
    occ.append(first_occ)

    i = first_occ
    while array[i-1] == val:
        i = i - 1
        occ.append(i)

    i = first_occ
    while array[i+1] == val:
        i = i + 1
        occ.append(i)

    return sorted(occ)

array = [1,1,1,4,4,4,4,4,6,6,9,11,11,15,15,15,15,17,21,34,34,56]

x = find_all_occurrence(1,array)
print(x)