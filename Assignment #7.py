'''
Lawrence Woods
2/19/2918
Assignment #7
'''

def convertStr2Int():
    string = input('Enter string to be checked:')
    try:
        number = int(string)
        print('String {:s} is converted  to number {:d}'.format(string, number))
    except ValueError:
        print("{:s} cannot be converted to a number.".format(string))

while True:
    try:
        convertStr2Int()
    except:
        pass
