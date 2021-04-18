
from collections import Counter
import math
import cleantext

alpha = " abcdefghijklmnopqrstuvwxyz"

with open("P.txt",'r') as f: 
                                        # initialize alphabet string and read plaintext from file
    file_ = f.readlines()
    words = cleantext.clean(file_, numbers=True , punct=True) 
    f.close()

def E(p): 
  
    c = [] 

    for index, char in enumerate(p):    # encryption function E iterates through plaintext p and assigns x, y, z, values for each char, returning cyphertext c 
        
        counter_ = Counter(p) 
    
        x =((index*index)+1)
        y = alpha.index(char.lower())*x
        z = counter_[char]
        w = (x,y,z)
        c.append(w)

    return(c)

with open("C.txt", 'a') as f:
    f.write(str(E(words)))
    f.close
