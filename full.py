from collections import Counter
import math
import cleantext
import time 

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


def D(c):

    p = ""

    for x, y, z in c:                   # decryption function D reverses the operations of E and returns c into p
    
        y = int(y/x)
        
        p += alpha[y]
        
    return(p)

print("\nStarting Encryption --> P.txt --> \n\n"+str(E(words))+"\n\nEncryption Successful --> Starting Decryption --> \n\n"+str(D(E(words)))+"\n\n Decryption Successfull")
    
