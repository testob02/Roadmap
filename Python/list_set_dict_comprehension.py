integer = [0,1,2,3,4]
binary = ['0','1','10','11','100']

binary_dict = {integer:binary for integer,binary in zip(integer,binary)}
print(binary_dict)


list_int = [1,-1,2,3,5,0,-7]
additive_inverse = [-i for i in list_int]
print(additive_inverse)


int_list = [1,-1,2,-2,3,-3]
sq_set = {i**2 for i in int_list}
print(sq_set)