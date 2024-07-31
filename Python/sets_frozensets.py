a = {1,2,4}
a.add(5)
a.add(4)
a.add(0)
print(a)
a = frozenset(a)
# wont work 
# a.add(6)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print('Union of both set is: ',set1|set2)
print('Intersection of both set is: ',set1&set2)
print('Difference between set1 and set2 is: ', set1-set2)
print('Difference between set2 and set1 is: ', set2-set1)

