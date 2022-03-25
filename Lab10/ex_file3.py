# file - I/O
# delete file

# open file from other directory
import os.path

try:
    f = open('C:\\Users\ICE Supinya\Desktop\demo_dasktop.txt')
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

# delete file

if os.path.exists("C:\\Users\ICE Supinya\Desktop\demo_dasktop.txt"):
    os.remove("C:\\Users\ICE Supinya\Desktop\t")
else:
    print('Could not find a file.')

