tuple1 = (11, [22, 33], 44, 55)

modified_tuple = tuple([222, *tuple1[1:]])

print(modified_tuple)
