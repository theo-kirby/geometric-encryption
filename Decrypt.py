import cleantext
import re

alpha = " abcdefghijklmnopqrstuvwxyz"
with open("C.txt", 'r') as f:
    
    file_ = f.read()
    f.close()

    
def D(c):
    

    nums = cleantext.clean(c, punct=True) 
    p = ""
    counter = 1
    l = []
    t = []
    for x in nums.split('), ('):

        if counter % 3 != 0:

            t.append(x)
            counter + 1
        
        elif counter % 3 == 0:

            t.append(x)
            l.append(t)
            counter = 1
    return(l)


print(D(file_))
print(file_)
