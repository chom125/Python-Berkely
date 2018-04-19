'''
Lawrence Woods
Assignment #5
2/5/2018
'''
'''
1. Using the keys method for dictionaries and the sort method for 
lists, write a for loop that prints the keys and corresponding values 
of a dictionary in the alphabetical order of the keys.
'''
exDict = {5:"Five",3:"Three",9:"Nine",10:"Ten",-1:"Minus one",2:"Two"}
for x in sorted(exDict.keys()):
    print(x,"\t",exDict[x])
    
#######################################################################

'''
2. As an alternative to the range function, some programmers like to 
 increment a counter inside a while loop and stop the while loop when 
 the counter is no longer less than the length of the array. 
 Rewrite the following code using a while loop instead of a for loop.
'''

a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [ ]
i = 0
while i<len(a) :
    big.append ( max ( a [ i ],b [ i ] ) )
    i+=1
print(big)

##########################################################################
'''
3. Write a loop that reads each line of a file. It should count the 
number of characters in each line and keep track of the total number 
of characters read. Once you have a total of 1,000 or more characters, 
break from the loop.(You can use a break statement to do this.)

'''

fileName = input("Enter file name: ")
try:
    f = open(fileName)
    lineNumber = 0
    totalCharacters = 0
    for line in f:
        print("Line",lineNumber,": ",len(line))
        totalCharacters += len(line)
        if(totalCharacters > 1000):
            break
        lineNumber += 1
    print("Total number of characters:",totalCharacters)
    f.close()
except Exception:
    print("File not found")

#####################################################################
'''
4. Modify the program written in question 3 so that it doesn't count 
characters on any line that begins with a pound sign (#).
'''

fileName = input("Enter file name: ")
try:
    f = open(fileName)
    lineNumber = 0
    totalCharacters = 0
    for line in f:
        print("Line",lineNumber,": ",len(line))
        if(not line.startswith("#")):
            totalCharacters += len(line)
        if(totalCharacters > 1000):
            break
        lineNumber += 1
    print("Total number of characters:",totalCharacters)
    f.close()
except Exception:
    print("File not found")









