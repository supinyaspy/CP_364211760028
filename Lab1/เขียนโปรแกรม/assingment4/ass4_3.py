# Assignment_4.1
f = open("A4Q1.txt", 'a')
i = int(input("Enter number: "))
num = 0
while num < i:
    if i % 5 == 0:
        num = num + 5
    f.write(str(num)+'\n')
f.close()


# Assignment_4.2
f = open("A4Q2.txt", 'a')
a = []
while True:
    c = int(input())
    if c == 1:
        break
    a.append(c)
f.write(str(a)+'\n')
f.close()