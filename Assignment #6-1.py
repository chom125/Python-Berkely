'''
Lawrence Woods
2/19/2018
Assignment #6

Write a function that accepts the name of a file and returns a tuple containing the number of lines,
words, and characters that are in the file. (Hint: Use the split function of the string module to help
you count the words in the file.)

Write a function that accepts an arbitrary number of lists and returns a single list with exactly one occurrence
of each element that appears in any of the input lists.

Use the map function to add a constant to each element of a list. Perform the same operation using a list
comprehension.

 For example, the list (1, 20, 300, 400) and constant 8, will result in: 9, 28, 308, 408

Write a function that will take a variable number of lists. Each list can contain any number of words.
This function should return a dictionary where the words are the keys and the values are the total count
of each word in all of the lists

 For example, if we are given the following lists:

 wl1 = ["double", "triple", "int", "quadruple"]
 wl2 = ["double", "home run"]
 wl3 = ["int", "double", "float"]

 the function should output the following dictionary (The order of the words is not important):
 {'float': 1, 'int': 2, 'quadruple': 1, 'home run': 1, 'triple': 1, 'double': 3}

Note, you may have to create an empty dictionary first (for example: dict = {}).


(Optional) Write a function that combines several dictionaries by creating a new dictionary
with all the keys of the original ones. If a key appears in more than one input dictionary, the
value corresponding to that key in the new dictionary should be a list containing all the values
encountered in the input dictionaries that correspond to that key.

'''

#function to get unique elements from arbitrary list
def arb_lists(*lists):

    # empty list
    t=[]

    # looping through every list
    for l in lists:

        # looping through every item in the individual list
        for item in l:

            # adding the element to the list
            if item not in t:
                t.append(item)

    # returning the list
    return t


# function to count element in the arbitary list
def arb_list_dict(*lists):

    # empty dictionary
    d={}

    # looping through every list
    for l in lists:

        # looping through every item in the individual list
        for item in l:

            # adding the element to the list
            if item not in d:
                d[item]=1
            else:
                d[item]+=1

    # returning the dictionary
    return d


# function for word,character, line count
def word_count(filename):

    # opening the file
    f=open(filename)

    # variables to store the lines, words, characters
    lines=0
    words=0
    characters=0

    # looping through every line
    for line in f:

        # counting the line
        lines+=1
        line=line.strip()

        data=line.split()

        # counting the words
        for word in data:
            words+=1

            # counting the characters
            for c in word:

                if c.isalpha():
                    characters+=1

    # closing the file
    f.close()

    # returning the result
    return(lines,words,characters)


#testing
if __name__=='__main__':

    # sample lists
    wl1 = ["double", "triple", "int", "quadruple"]
    wl2 = ["double", "home run"]
    wl3 = ["int", "double", "float"]

    # calling the function
    r=arb_lists(wl1,wl2,wl3)
    print("\nresult for arb_lists: ",r)


    s=[10,20,30,40,50]

    # adding the constants to the list using map function
    l2=list(map(lambda x:x+3,s))
    print("\nlist created by map function: ",l2)


    # adding the constants to the list using list comprehension
    l3=[i+3 for i in s]

    print("\nlist created by list comprehension:",l3)

    # calling the function
    print("\nresult for arb_list_dict function: ",arb_list_dict(wl1,wl2,wl3))

    # calling the function
    print("\nresult for word_count function: ",word_count('sample.txt'))