def fact_decor(func):
    def wrapper(x):
        if type(x) == int and x >= 0:
            return func(x)
        else:
            raise Exception('Non-negative Integer')
        
    return wrapper

@fact_decor
def factorial(n):
    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    return n * factorial(n-1)

    return result

#factorial(1.354)
#factorial(-1)
print(factorial(5))
