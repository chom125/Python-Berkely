"""
Lawrence Woods
2/24/2018
Final Project
"""

os.path.splitext() for getting ext
import os
import sys
import pprint

dirname = raw_input("please enter a dir: ")

if not os.path.isdir(dirname):
    print "can't find directory", dirname
    sys.exit()
else:
    print "reading directory", dirname, "\n"

ext_dict = {} #get a dict with all the different file extensions as keys

for root, dirs, files in  os.walk(dirname):
    for singlefile in files:
        if not ext_dict.get(os.path.splitext(singlefile)[1]): #if ext is not in the dict, add it with an empty list as a value
            ext_dict[os.path.splitext(singlefile)[1]] = []
        ext_dict[(os.path.splitext(singlefile)[1])] += [(singlefile, os.path.getsize(os.path.join(root, singlefile)))] #add file and filesize as keys

pprint.pprint(ext_dict.keys())
#dict looks like:
# {'.gif': [('02AerialDetail.gif', 242353),
#           ('10-DJ-50x50.gif', 5645),
#           ('4F4.gif', 1053),
#           ('Aerial.gif', 183501),
#           ('BFF_HipHopBooty1_6_14.gif', 75832),

for ext in ext_dict.keys():
    totalsize = 0
    avg = 1
    for singlefile,size in ext_dict[ext]:
        totalsize += size
        avg = totalsize/len(ext_dict[ext])
    print "TOTAL  NUMBER  OF", ext, "IS", len(ext_dict[ext]) # .gif 14
    print "AVG  FILESIZE FOR", ext, "IS", avg
    print "SMALLEST FILE FOR", ext, "IS", sorted(ext_dict[ext],key=lambda x:x[1])[0][1]
    print "LARGEST  FILE FOR", ext, "IS", sorted(ext_dict[ext],key=lambda x:x[1])[-1][1]
    print "\n"