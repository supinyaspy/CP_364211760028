"""
Name: {นางสาวสุภิญญา ศรีเจริญ}
SID: {364211760028}
Group: {MIT211}
"""

"""
Question 4:
เขียนโปรแกรมรับ input ที่เป็นจำนวนเต็ม 10 จำนวน และตรวจสอบว่าตัวเลขนั้นเป็นจำนวนคี่หรือไม่
ถ้าเป็นจำนวนคี่ ให้นำไปเก็บไว้ในตัวแปรชนิด List ชื่อ myOdd
จากนั้นแสดงผลทางหน้าจอ output

ตัวอย่างผลลัทพ์
Input 10 integer: 11 12 13 14 15 16 17 18
Output:
Odd: 11 13 15 17

(10 คะแนน)
"""
number = int(input("ป้อนตัวเลขจำนวนเต็มบวก : "))

if number % 2 == 0:
    print(f"{number} เป็นเลขคู่ (even)")
else:
    print(f"{number} เป็นเลขคี่ (odd)")