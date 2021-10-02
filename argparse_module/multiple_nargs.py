import argparse

parser = argparse.ArgumentParser()

# parser.add_argument('--values', type=int, nargs=3)  # nargs คือ การใส่ข้อมูลหลายข้อมูลตามที่เรากำหนด
#                                                     # และต้องใส่ตามจำนวนนั้น

# args = parser.parse_args()

# sum = sum(args.values)
# print('Sum is', sum)


# ************************************************************
parser.add_argument('--values', type=int, nargs='+') # หากใส่ nargs = '+' คือ ใส่กี่ข้อมูลก็ได้
args = parser.parse_args()
sum = sum(args.values)
print('Sum is', sum)
# ------------------------------------------------------------