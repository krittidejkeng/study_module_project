"""
เป็นฟังก์ชันที่ช่วยในการทดสอบ แต่ละสมาชิกว่าเป็น True หรือ False

filter(function, iterable)
function - a function
iterable - an iterable like sets, lists, tuples etc.
"""


seq = [0, 1, 2, 3, 5, 8, 13]
  
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
  
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))