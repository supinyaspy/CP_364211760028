# Assignment 3 Q1

"""
Name: {นางสาวสุภิญญา ศรีเจริญ}
SID: {364211760028}
Group: {MIT211}
"""

def getNumber():
    mynumber = []
    for x in range(3):
        mynumber.append(int(input(f'Enter integer [{x+1}]: ')))
    return mynumber
def totalValue(var):
    total = 0
    for x in var:
        total+=x
    return total

mynum = getNumber()
print(f'The data from user: {mynum}')
print(f'The summation of those integer is: {totalValue(mynum)}')
