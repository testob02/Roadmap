def swap(one, two, array):
    array[one], array[two] = array[two], array[one]

def partition(array,start,end):
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            swap(i,j,array)
            i += 1
    
    swap(i,end,array)
    return i

def quick_sort(array,start,end):
    if start >= end or start < 0:
        return
    
    p = partition(array,start,end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
    
array = [11,9,29,7,2,30,15,28]
quick_sort(array,0,len(array)-1)
print(array)