import csv
from collections import Counter
import math
import cleantext

alpha = " abcdefghijklmnopqrstuvwxyz"

with open('p.csv',mode='r') as f:     # Read plaintext from file (p.csv)    

    file_ = f.readlines()
    words = cleantext.clean(file_, numbers=True , punct=True) 
    f.close()

def Encrypt(p): 
  
    c = []  

    with open('c.csv', mode='w') as f_:


        fieldnames = ['x','y','z']
        writer = csv.DictWriter(f_, fieldnames=fieldnames)
        writer.writeheader()
        print(" \n Encryption of Plaintext (p.csv) -> Cyphertext (c.csv) : \n") 
 
        for index, char in enumerate(p):   
        
            counter_ = Counter(p) 
    
            x =((index*index)+1)
            y = alpha.index(char.lower())*x
            z = counter_[char]
            w = (x,y,z)
            c.append(w)
        
            writer.writerow({'x': x, 'y': y, 'z': z})
 
    print(c)

Encrypt(words)


f.close()   
