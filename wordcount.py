print("Input file name below. The file MUST be in the same directory as the program")
filename = input()

import sys
import re
charcount=0
def charcounter(x):
    global charcount
    if x <= 25: 
        with open(filename, 'r') as file:
            data = file.read().replace('\n', '').lower()
            y = data.rsplit()
            ordah = chr(ord('a') + x)
            for i in y:
                if i.startswith(ordah):
                    charcount += 1
        counterplus=""
        counterplus+=str("Words with letter " +str(ordah)+ ": " +str(charcount))
        print(counterplus)
        #charcount's value is reinitialized to 0
        charcount=0
        #recursion function will loop over each individual letter
        return charcounter(x+1)
    else:
        return "Completion"

charcounter(0)