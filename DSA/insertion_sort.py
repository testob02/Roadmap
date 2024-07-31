def insertion_sort(array):
    for i in range(1,len(array)):
        pivot = array[i]
        j = i - 1
        while j >= 0 and pivot < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = pivot

stream = []
while True:
    inp = int(input())
    stream.append(inp)
    insertion_sort(stream)
    i = len(stream)
    mid = i // 2
    if i % 2 == 0:
        median = (stream[mid] + stream[mid-1]) / 2
    else:
        median = stream[mid]
        
    print(f'Median of {stream} is: {median}')
    