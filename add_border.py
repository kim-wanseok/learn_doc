import sys

# dkf

def print_with_border(string):
    """
    This is a function to print border line around the string
    """
    print('*'* (len(string) + 4))
    print('* ' + string + ' *')
    print('*'* (len(string) + 4))

