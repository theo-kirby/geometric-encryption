import numpy
import csv
import cleantext
import re

alpha = " abcdefghijklmnopqrstuvwxyz"
    
with open('c.csv', 'r') as f:     # Read cyphertext from file (c.csv)
    reader = csv.DictReader(f)
    f.close()
        
def Decrypt(c):

    p = ""    
    
    with open('c.csv', 'r') as f:

        reader = csv.DictReader(f)
        lines = 0
        print(" \n Decryption of Cyphertext (c.csv) : \n")

        for row in reader:
            
                
                    
                x = row['x']
                y = row['y']
                z = row['z']

                x = int(x)

                if y != 0:
                    y = int(y)/x
                        
                y = alpha[(int(y))]

                x = int(numpy.sqrt((int(x)-1)))

                p += y
    print(p)

Decrypt(reader)
f.close()
