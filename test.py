import types
# fact = True
# no = False
# test = [1,'k','keng',fact,12,no,3]
# # test = [1,3,33,12,34,56,11,19,21,34,15]
# listofNum = [1,3,33,12,34,56,11,19,21,34,15]
# m = lambda x : type(x) is types.StringType , listofNum
# m = map(lambda x : type(x) in test , listofNum)
# print('m is',m)
# for x in m:
#     print('x is',x)

# m = lambda type(a) in listofNum : 


# fact = True
# no = False
# test = [1,'k','keng',fact,12,no,3]
# # test = [1,3,33,12,34,56,11,19,21,34,15]
# listofNum = [1,3,33,12,34,56,11,19,21,34,15]
# m = map(lambda x:x : type(x+1) in [1,'k','keng',fact,12,no,3] , listofNum)
# # m = map(lambda x : True if type(x+1) in [1,'k','keng',fact,12,no,3] else False, listofNum)
# print('m is',m)

# x = [1,10,5,4]
# x = map(lambda y: y+1, x)
# print('k is',x)



# x = lambda d:d*d
# # import types
# print (type(x) is types.LambdaType)






lst = [10, 50, 75, 83, 98, 84, 32] 
res = list(map(lambda x:x, lst))

ans = bool(map(lambda x : True if type(res) in [12,3,'ll'] else False,res))
print(res) 





# m.inplace = list(filter(lambda m : type(m) in [nn.Hardswish, nn.LeakyReLU, nn.ReLU, nn.ReLU6, nn.SiLU, Detect, Model] and x < 20, listofNum))