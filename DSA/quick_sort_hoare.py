def swap(one, two, arr):
    if one != two:
        arr[one], arr[two] = arr[two], arr[one]
    
def partition(array,start,end):
    pivot = start

    while start < end:
            while start < len(array) and array[start] <= array[pivot]:
                start+=1
            
            while array[end] > array[pivot]:
                end-=1
            
            if start < end:
                swap(start,end,array)
    
    swap(pivot,end,array)

    return end
def quick_sort(array,start,end):
    if start < end:
        p1 = partition(array,start,end)
        quick_sort(array,start,p1-1)
        quick_sort(array,p1+1,end)


array = [5,2,9,3,19,50,22,98,15]
quick_sort(array,0,len(array)-1)
print(array)