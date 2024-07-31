def selection_sort(arr, key):
    for i in range(len(arr)):
        min_idx = i
        for j in range(min_idx,len(arr)):
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j
        
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
def multi_level_sort(arr, keys):
    for key in keys[-1::-1]:
        selection_sort(arr, key)


# tests = [
#         [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
#         [],
#         [1,5,8,9],
#         [234,3,1,56,34,12,9,12,1300],
#         [78, 12, 15, 8, 61, 53, 23, 27],
#         [5]
#     ]
# for elements in tests:
#     selection_sort(elements)
#     print(elements)

test = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

multi_level_sort(test, ['First Name','Last Name'])
print(test)