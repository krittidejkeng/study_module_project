# numbers = [12, 34, 1, 4, 4, 67, 37, 9, 0, 81]

numbers = ['k','asd','keng','llll',1,4,5]

numbers = [True, False, False,True]
# simple loop
# result = []
# for index in range(len(numbers)):
#     if numbers[index] > 5:
#         result.append(numbers[index])
# print(result) 

# slightly cleaner
# result = []
# for number in numbers:
#     if number > 5:
#         result.append(number)
# print(result)  #Prints [12, 34, 67, 37, 9, 81]

# ******************************************************************************
# Enter List Comprehension
# result = [number for number in numbers if number]
# print(result) #Prints []
# ------------------------------------------------------------------------------



# *****************************************************************************
num = [1,23,4,123,5,7,42,78]
result = []
for item in num:
    new_item = num(item)
    result.append(new_item)
print(result) 

# result = [do_something_with(item) for item in item_list]
# -----------------------------------------------------------------------------