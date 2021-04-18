import cleantext


with open("C.txt", 'r') as f:
    
    file_ = f.read()
    nums = cleantext.clean(file_, punct=True) 
    print(nums)
    f.close()

l = []

def D(c):

    p = ""

    for x, y, z in c:                   # decryption function D reverses the operations of E and returns c into p
    
        y = int(y/x)
        
        p += alpha[y]
        
    return(p)

for index, char in enumerate(nums):
    
    t = nums[index], nums[index+1], nums[index+2]
    l.append(t)

print(l)
