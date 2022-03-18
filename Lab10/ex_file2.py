# File - create and write

"""
mond
x - create
a - create and write from end of file
w- create and overwrite
"""

# create file
try:
    f = open('demo2.txt','x') # empty file
    print(f.read())
except Exception as e:
    print(e)
    print('This file name is already exist. ')
else:
    print('Create file successfull.')

# create file with mode 'a'
try:
    f = open('demo6.txt','a')
    f.write("Writing contents with mode 'a' .... MIT211")
except Exception as e:
    print(e)
else:
    print('writing contents already.')
finally:
    f.close()



try:
    f = open('demo7.txt','w')
    f.write("delete and writing new contents with mode 'w' .... MIT211")
except Exception as e:
    print(e)
else:
    print('writing contents already.')
finally:
    f.close()