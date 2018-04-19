'''
Lawrence Woods
2/18/2018
Assignment #9

Using os.walk, write a script that will print the filenames of zero length files. It should also print
the count of zero length files.

Write a script that will list and count all of the images in a given HTML web page/file. You can assume that:
Each image file is enclosed with the tag <img and ends with >
The HTML page/file is syntactically correct
'''

import os

count = 0
 for root, dirs, files in os.walk(".", topdown = False):
     for name in files:
         if os.path.getsize(name) == 0:
            print(name)
            count = count + 1
 print("Number of files with zero length:",count)
 count = 0
 try:
 file = open("sample.html","r")
 for line in file:
       if "<img" in line:
           count = count + 1
 print("Number of images:",count)
 except:
 print("Error opening file")
