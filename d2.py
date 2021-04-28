import cleantext
with open("C.txt", 'r') as f:
    
    file_ = f.read()
    nums = cleantext.clean(file_, punct=True) 
    print(nums)
    f.close()

l = []
t = ()
def D(c):

    p = ""

    for x, y, z in c:                   # decryption function D reverses the operations of E and returns c into p
    
        y = int(y/x)
        
        p += alpha[y]
        
    return(p)
for index, num in enumerate(nums):

    if index % 3 != 0:
        t += tuple(num)    
    else:
        t += tuple(num)
        l.append(t)
        t = ()
print(l)
