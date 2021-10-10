# print (type(__name__))
# print (__name__)


"""
ถ้าหาก เป็นการเขียนเพียวๆ ไม่มีการอ้างอิงถึงตัว script อื่นๆ __name__ จะเท่ากับ __main__
"""
def func1():
   print ('The value of __name__ is ' + __name__)
if __name__ == '__main__':
   func1()


"""
ถ้าหากมีการอ้างอิงถึง script ตัวอื่น ตัว __name__ จะทำการเปลี่ยนเป็นตัว script ที่อ้างถึง ดังตัวอย่าง
"""
import standalone as sa

print('Running the imported script')
sa.func1() # The value of __name__ is standalone

print('\n')
print('Running the current script')
print ('The value of __name__ is ' + __name__)