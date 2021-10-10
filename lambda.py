"""
lambda arguments : expression
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

The expression is executed and the result is returned:
"""

# ****************************************************************************
# x = lambda a : a + 10
# print(x(5))

# y = lambda a, b : a * b
# print(y(5, 6))
# ----------------------------------------------------------------------------

"""
if, else & elif in Lambda Functions
lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>
"""

# ****************************************************************************
# listofNum = [1,3,33,12,34,56,11,19,21,34,15]

# listofNum = list(filter(lambda x : x > 10 and x < 20, listofNum))
# print('Filtered List : ', listofNum)
# ----------------------------------------------------------------------------

str = 'keng'
num = 1
listofNum = [1,3,'name',False,'haha','lol',True,True]

listofNum = list(filter(lambda x : type(x) in [int,type(str)], listofNum))
print('Filtered List : ', listofNum)