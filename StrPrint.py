import sys

class StringPrint:
    '''
    
    This module is print function package to decoration for string
    
    '''
    
    @classmethod
    def print_mark(cls, _str, mark):
        cls.mark = mark
        print(cls.mark * ( len(_str)+4 ) )
        print(cls.mark + " " + _str + " " + cls.mark)
        print(cls.mark * ( len(_str)+4 ) )

    @classmethod
    def print_ab(cls, _str):
        """
        This is a function to print asterisk border line around the string
        """
        cls.print_mark(_str, "*")

    @classmethod
    def print_dlb(cls, _str):
        """
        This is a function to print double line border line around the string
        """
        cls.print_mark(_str, "=")

    @classmethod
    def print_list(cls, _str, index=None):
        """
        This is a fucntion to find string value and index number in the string
        Input parameters are string and integer value.
        The str argument is String, index is integer
        """
        str_list = _str.split()
        # self.index = index
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
            raise ZeroIndexError("ZeroIndexError: should input over zero. Plese check index")
        if self.index > len(self.s_list):
            raise OverIndexError("OverIndexError: list index out of range")


if __name__ == '__main__':
    l = len(sys.argv)-1
    functions = {'-a': StringPrint.print_ab, '-d': StringPrint.print_dlb, '-m' : StringPrint.print_mark, '-s': StringPrint.print_list}
    if l == 1:
        print(sys.argv[1])    
    elif l <= 3:
        opt = sys.argv[1]
        func = functions[opt]
        if l == 2:
            s = sys.argv[2]
            if opt == '-a' or opt =='-d':
                func(s)
            elif opt == '-s':
                func(s)
            else:
                print("plese check option value")
                exit()
        else:
            sub_opt = sys.argv[2]
            s = sys.argv[3]
            if opt == '-m':
                func(s, sub_opt)
            elif opt == '-s':
                func(s, int(sub_opt))
            else:
                print("plese check option value")
                exit()
    else:
        print("please check command")
        exit()
