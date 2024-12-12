#! python3

'''
See some of the different ways that an index can be used to find elements from a tuple or list:

The index is usually a positive, number, indicating position from the start of the tuple/list,
but can also be a negative number, indicating position from the end of the tuple/list
'''

myTuple = ('Alpha', 'Baker', "Charlie", "Delta", "Echo","Foxtrot","Golf")
print("\n======")
print(myTuple)
print(f" tuple[0] is {myTuple[0]}")
print(f" tuple[1] is {myTuple[1]}")
print(f" tuple[-1] is {myTuple[-1]}")
print(f" tuple[-3] is {myTuple[-3]}")
'''
A range of values from a tuple can be printed using the : to indicate the
beginning and ending.
The beginning and ending can be omitted, which would indicate everything
to the beginning or to the end
'''
print("\n== For printing a range, note which indexes are included and which are not...")
print("== the 1st index is inclusive and the index after the : is not included")
print(f" tuple[1:3] is {myTuple[1:3]}")
print(" tuple[:2] is ", end="")
print(myTuple[:2])
print(" tuple[2:] is ", end="")
print(myTuple[2:])
print(f" tuple[-4:-1] is {myTuple[-4:-1]}")



