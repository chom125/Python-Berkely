'''
Lawrence Woods
2/21/2018
Complete this assignment and attach the .py and/or .txt file(s) to the drop box for this
module, which you'll find near the end of the module. Please be sure to include your last
name and the course number in the file name of the document, like so: "your name X442.3 Assignment 10."

1. Write a simple Rectangle class. It should do the following:

        Accepts length and width as parameters when creating a new instance
        Has a perimeter method that returns the perimeter of the rectangle
        Has an area method that returns the area of the rectangle
        Don't worry about coordinates or negative values, etc.

Python provides several modules to allow you to easily extend some of the basic objects in the
language. Among these modules are UserDict, UserList, and UserString. (Refer to the chart in Topic 10.3
to see what the methods you need to override look like. Also, since UserDict and UserList are part of the
collection module, you can import them using from collections import UserDict and from collections import UserList.)

2. Using the UserList module, create a class called Ulist, and override the __add__, append, and extend methods
so that duplicate values will not be added to the list by any of these operations.

3. (Extra Credit) Using the UserDict module, create a class called Odict, which will be just like a dictionary
but will "remember" the order in which key/value pairs are added to the dictionary. (Hint: Override the built-in _
setitem__ method.) Create a new method for the Odict object called okeys, which will return the ordered keys.
'''


# 1. Rectangle Class in python3, this will return area and perimeter:

class Rectangle:
        def __init__(self,length,width):
                self.length=length
                self.width=width
        def perimeter(self):
                perimeter_value= 2*(self.length+self.width)
                return perimeter_value
        def area(self):
                return self.length*self.width
rect_obj=Rectangle(5,10)
print("The perimeter of rectangle is: ",rect_obj.perimeter())
print("The are of rectangle is: ",rect_obj.area())


# 2 & 3) UserDict and UserList:

from collections import UserDict

class Odict(UserDict):
    def __init__(self, data = {}, **kw):
        UserDict.__init__(self)
        self.update(data)
        self.update(kw)
        self.keylist = []

    def __setitem__(self,key,value):
        self.data[key] = value
        self.keylist.append(key)

    def okeys(self):
        return self.keylist


myDict = Odict()
myDict['d'] = 'value5'
myDict['a'] = 'value4'
myDict['e'] = 'value6'

print(myDict.okeys())

from collections import UserList
class Ulist(UserList):
    def __init__(self, data = [], **kw):
        UserList.__init__(self)
        self.data = data

    def __add__(self, newvalue):
        for item in newvalue:
            if item in self.data:
                print ("%r already exists, not adding." % item)
            else:
                self.data += [item]
        return self.data

    def append(self,newvalue = None):
        if newvalue in self.data:
            print ("%r already exists, not adding." % newvalue)
        else:
            return self.data.append(newvalue)

    def extend(self, newvalue = []):
        for item in newvalue:
            if item in self.data:
                print ("%r already exists, not adding." % item)
            else:
                return self.data.extend(item)
        return self.data

mylist = Ulist([1,2,3])
#mylist.__add__([5,6])
#mylist.append('a')
#mylist.append([3])
#mylist.extend([1,2,3,'a'])
print( mylist)


