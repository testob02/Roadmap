def bubble_sort(array,key):
    for i in range(len(array)-1):
        swapped = False
        for j in range(len(array)-1-i):
            if array[j][key] > array[j+1][key]:
                swapped = True
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp
        if not swapped:
            break

array = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort(array,'transaction_amount')
print(array)
