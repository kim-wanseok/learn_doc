import collections

# iterable 한 타입
var_list = [1, 3, 5, 7]
print('list is ', isinstance(var_list, collections.Iterable))

var_dict = {"a": 1, "b":1}
print('dictionary is ', isinstance(var_dict, collections.Iterable))

var_set = {1, 3}
print('set is ', isinstance(var_set, collections.Iterable))

var_str = "abc"
print('string is ', isinstance(var_str, collections.Iterable))

var_tuple = (1, 3, 5, 7)
print('tuple is ', isinstance(var_tuple, collections.Iterable))

var_range = range(0,5)
print('range is ', isinstance(var_range, collections.Iterable))


# iterable하지 않은 타입
var_int = 932
print('int is ', isinstance(var_int, collections.Iterable))

var_float = 10.2
print('float is ', isinstance(var_float, collections.Iterable))

var_none = None
print('None is ', isinstance(var_none, collections.Iterable))