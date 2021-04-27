import sys

'''
This module is print function package to decoration for string
'''

class ZeroIndexError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class OverIndexError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class CheckIndex:
    def __init__(self, index, l_list):
        self.index = index
        self.l_list = l_list
    def check(self):
        if self.index <=0:
            raise ZeroIndexError("ZeroIndexError: should input over zero. Plese check index")
        if self.index > len(self.l_list):
            raise OverIndexError("OverIndexError: list index out of range")

def print_with_ab(string):
    """
    This is a function to print asterisk border line around the string
    """
    print('*'* (len(string) + 4))
    print('* ' + string + ' *')
    print('*'* (len(string) + 4))

def print_with_dlb(string):
    """
    This is a function to print double line border line around the string
    """
    print('='* (len(string) + 4))
    print('= ' + string + ' =')
    print('='* (len(string) + 4))

def print_list_value(s, index=None):
    """
    This is a fucntion to find string value and index number in the string
    """
    str_list = s.split()
    if index != None:
        try:
            CheckIndex(index, str_list).check()
            if index == 1:
                print(f'The {index}st value is " {str_list[index-1]} "')
            elif index == 2:
                print(f'The {index}nd value is " {str_list[index-1]} "')
            else:
                print(f'The {index}th value is " {str_list[index-1]} "')
        except ZeroIndexError as e:
            print(e); exit()
        except OverIndexError as e:
            print(e); exit()
    
    else:
        index = 0
        for val in str_list:
            if index == 0:
                print(f'[ {val} ] is the {index+1}st value in string')
            elif index == 1:
                print(f'[ {val} ] is the {index+1}nd value in string')
            else:
                print(f'[ {val} ] is the {index+1}th value in string')
            index = index + 1

s = sys.argv[1]
s_list = s.split()
print_with_ab(s)
print_with_dlb(s)
print_list_value(s_list)
print_list_value(s_list, 1)
