def shell_sort(arr):
    size = len(arr)
    div = 2
    gap = size // div
    while gap > 0:
        del_index = []
        for i in range(gap, size):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] >= temp:
                if arr[j-gap] == temp:
                    del_index.append(j)
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        del_index = list(set(del_index))
        del_index.sort(reverse=True)
        if del_index:    
            for idx in del_index:
                del arr[idx]
    
        size = len(arr)
        div *= 2
        gap = size // div

arr = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
shell_sort(arr)
print(arr)