# Assignment 3 Q2

"""
Name: {นางสาวสุภิญญา ศรีเจริญ}
SID: {364211760028}
Group: {MIT211}
"""

def getNumber():
    mylist = []
    for x in range(1):
        mylist.append(int(input(f'Enter integer : ')))
    return mylist
def myfunction(var):
    total = 0
    for x in var:
        e = x ** 2
        total = total + e
    return total


mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The result of squaring is: {myfunction(mynum)}')