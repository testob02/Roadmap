def square():
    start = 0
    while True:
        start += 1
        yield start **2

for n in square():
    if n <= 81:
        print(n)
    else:
        break