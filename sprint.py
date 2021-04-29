import sys

<<<<<<< HEAD
def sprint_ab(s):
=======
def sprint_ab(str):
>>>>>>> f95eca0b99d1545059d90216d9e6268cf4bac27b
    print("*" * ( len(s)+4 ) )
    print("* " + s + " *")
    print("*" * ( len(s)+4 ) )

def sprint_dlb(s):
    print("=" * ( len(s)+4 ) )
    print("= " + s + " =")
    print("=" * ( len(s)+4 ) )

def sprint(s, mark):
    print(mark * ( len(s)+4 ) )
    print(mark + " " + s + " " + mark)
    print(mark * ( len(s)+4 ) )

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
    def __init__(self, index, s_list):
        self.index = index
        self.s_list = s_list
    def check(self):
        if self.index <= 0:
<<<<<<< HEAD
            raise ZeroIndexError("ZeroIndexError: should input over zero. Plese check index")            
=======
            raise ZeroIndexError("ZeroIndexError: should input over zero. Plese check index")
>>>>>>> f95eca0b99d1545059d90216d9e6268cf4bac27b
        if self.index > len(self.s_list):
            raise OverIndexError("OverIndexError: list index out of range")


def sprint_list(s, index=None):
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

if __name__ == '__main__':
    s = sys.argv[1]
    # sprint_ab(s)
    sprint_list(s, 4)
# s = sys.argv[1]
# sprint_ab(s)
# # sprint("Hello world", "$")