from pathlib import Path

path = Path("runs/detect/test.txt")

if path.exists():
    print("file exists")
else:
    print("file not exists")

"""
การแสดงผลนี้จะออกเป็น file exists เพราะว่าเจอไฟล์ แต่ถ้าหากไม่เจอไฟล์จะเป็น file not exists
"""
