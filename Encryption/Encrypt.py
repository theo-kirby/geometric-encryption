import csv
import sys
import getopt
from collections import Counter
import math
import cleantext

alpha = " abcdefghijklmnopqrstuvwxyz"
words = ""
inputfile = ''
outputfile = ''

def Encrypt(p): 
    
    c = []
    
    with open(inputfile, mode='r') as f:     # Read plaintext from file (p.csv)    
        global words
        file_ = f.readlines()
        words = cleantext.clean(file_, numbers=True , punct=True) 
        f.close()
  
    with open(outputfile, mode='w') as f_:

        fieldnames = ['x','y','z']
        writer = csv.DictWriter(f_, fieldnames=fieldnames)
        writer.writeheader()
        print(" \n Encryption of Plaintext ("+inputfile+") -> Cyphertext ("+outputfile+"+) : \n") 
 
        for index, char in enumerate(words):   
        
            counter_ = Counter(p) 
    
            x =((index*index)+1)
            y = alpha.index(char.lower())*x
            z = counter_[char]
            w = (x,y,z)
            c.append(w)
        
            writer.writerow({'x': x, 'y': y, 'z': z})
 
    print(c)

def main(argv):
       
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      
   except getopt.GetoptError:
      print('Encrypt.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
      
   for opt, arg in opts:
       
      if opt == '-h':
         print('Encrypt.py -i <inputfile> -o <outputfile>')
         sys.exit()
         
      elif opt in ("-i", "--ifile"):
        global inputfile
        inputfile = arg
         
      elif opt in ("-o", "--ofile"):
        global outputfile
        outputfile = arg
         
if __name__ == "__main__":
    
   main(sys.argv[1:])
   Encrypt(words)