# Assignment 3 Q3

"""
Name: {นางสาวสุภิญญา ศรีเจริญ}
SID: {364211760028}
Group: {MIT211}
"""

op = ['+', '-', '*', '/']
def calculator():
    a = input('Enter A : ')
    b = input('Enter B : ')
    op = input('Enter OP :')
    if op == '+':
        return 'a+b'
    elif op == '-':
        return 'a-b'
    elif op == '*':
        return 'a*b'
    else:
        return 'a/b'

cal = calculator()
print(cal)