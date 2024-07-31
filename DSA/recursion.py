###     SUMMING A LIST
# def summing(arr):
#     size = len(arr)

#     if size == 1:
#         return arr[0]
    
#     else:
#         return arr[0]  + summing(arr[1:])

# arr = [3,2,1]
# print(summing(arr))


###     CONVERTING NUMBER BASES
# def convert_base(num, base):
#     char_set = '0123456789ABCDEF'
#     whole = int(num / base)
#     rem = num % base

#     if whole == 0:
#         return char_set[rem]
    
#     return convert_base(whole,base) + char_set[rem]

# x = convert_base(820,2)
# print(x)


###     SUMMING LIST OF LISTS
# def summing(arr):
#     if len(arr) == 1:
#         if type(arr[0]) == list:
#             return summing(arr[0])
#         else:
#             return arr[0]
#     else:
#         if type(arr[0]) == list:
#             return summing(arr[0]) + summing(arr[1:])
#         else:
#             return arr[0] + summing(arr[1:])
    

# test = [1, 2, [3,4], [5,6], [7,8,9], [10]]
# print(summing(test))


###     FACTORIAL
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)
    
# x = factorial(5)
# print(x)


###     FIBONACCI
# def fibonacci(num):
#     if num == 0:
#         return 0
#     if num == 1:
#         return 1

#     return fibonacci(num-1) + fibonacci(num-2)


###     DIGITS SUM
# def digits_sum(num): 
#     if int(num / 10) == 0:
#         return num % 10
    
#     return (num % 10) + digits_sum(int(num / 10))

# print(digits_sum(345))


###     SUM OF EVEN NUMBERS
# def sum_series(n):
#     if n <= 0:
#         return 0
    
#     return n + sum_series(n-2)
    
# print(sum_series(20))


###     HARMONIC SUM
# def harmonic_sum(num):
#     if num == 1:
#         return 1 / num
    
#     return (1 / num) + harmonic_sum(num - 1)

# print(harmonic_sum(5))


###      GEOMETRIC SUM
# def geom_sum(num):
#     if num == 0:
#         return 1
    
#     return (1 / (2 ** num)) + geom_sum(num - 1)

# print(geom_sum(3))


###     POWER
# def power(a,b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
    
#     if a == 1:
#         return 1
#     elif a == 0:
#         return 0
    
#     return a * power(a, b-1)

# print(power(3,4))


# ###     GREATEST COMMON DIVISOR
# def gcd(a,b):
#     maxi = max(a,b)
#     mini = min(a,b)

#     if maxi % mini == 0:
#         return mini
    
#     return gcd(mini, maxi % mini)


# print(gcd(96,112))