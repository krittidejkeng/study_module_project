"""
map() function returns a map object(which is an iterator) of the results 
after applying the given function to each item of a given iterable (list, tuple etc.)

map(fun, iter)
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 

"""

# **************************************************************************
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
# --------------------------------------------------------------------------


numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))