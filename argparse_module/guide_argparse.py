import argparse

parser = argparse.ArgumentParser()  #ใช้เริ่มต้น เพื่อใช้สำหรับการ เพิ่ม argument

"""
add_argument(name, type, required,help)
name คือ ชื่อสำหรับส่งค่าใน cmd 
type คือ ประเภคของข้อมูล
required คือ เป็นประเภค boolean ที่คอยบอกว่าต้องส่เป็นหลักไหม 
help คือ เอาไว้ช่วยเมื่อเราไม่รู้ name โดยการใช้ -h
"""
parser.add_argument('--x', type=int, required=True, help='the frist value')
parser.add_argument('--y', type=int, required=True, help="the second value")
args = parser.parse_args()
product = args.x * args.y

print('product:',product)