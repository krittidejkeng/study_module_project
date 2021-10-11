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

# ************************************* if else in lambda fn *****************************************
# listofNum = [1,3,33,12,34,56,11,19,21,34,15]
# ans = lambda x : True if (x > 10 and x < 20) else False
# print('ans is',type(ans))
# ---------------------------------------------------------------------------------------------------

# *********************************** condition without if else in lambda fn *************************
listofNum = [1,3,33,12,34,56,11,19,21,34,15]
listofNum = list(filter(lambda x : x > 10 and x < 20, listofNum))
print('Filtered List : ', type(listofNum))
# ---------------------------------------------------------------------------------------------------


"""
Using if, elif & else in a lambda function
lambda <args> : <return Value> if <condition > ( <return value > if <condition> else <return value>)
"""
# ************************************ if else in a lambda function ********************************
converter = lambda x : x*2 if x < 10 else (x*3 if x < 20 else x)
print('convert 5 to : ', converter(5))
print('convert 13 to : ', converter(13))
print('convert 23 to : ', converter(23))
# --------------------------------------------------------------------------------------------------


# str = 'keng'
# num = 1
# listofNum = [1,3,'name',False,'haha','lol',True,True]

# listofNum = list(filter(lambda x : type(x) in [int,type(str)], [1,3,'name',False,'haha','lol',True,True]))
# print('Filtered List : ', listofNum)