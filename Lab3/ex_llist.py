# List

x = 100
print(x)
x = 200
print(x)

mylist = ['apple', 'banana', 'cherry']
print(mylist, type(mylist))
print(f'Length of mylist = {len(mylist)}')

# access data in list
# index
print(mylist[0])  # apple
print(mylist[1])  # banana
print(mylist[2])  # cherry
# negative index
print(mylist[-1])  # cherry
print(mylist[-2])  # banana
print(mylist[-3])  # apple
# range index
mynum = [10, 20, 30, 40, 50, 60, 70 ]
print(mynum)
print(mynum[2:5]) # 2-4
print(mynum[1:6]) # 1-5
print(mynum[:5]) # 0-4
print(mynum[3:]) # 3-end
# negative range index
print(mynum[-5:-1])
# loop
# for
for x in mynum:
    print(x,type(x))
for x in range(len(mynum)):
    print(mynum[x])

# while
i = 0
while i < len(mynum):
    print(mynum[i])
    i+=1