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

# Enter List Comprehension
result = [number for number in numbers if number]
print(result) #Prints []