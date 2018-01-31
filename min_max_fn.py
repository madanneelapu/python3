#create a function that takes a list/set/tuple and returns min and max value

def min_max(data):
    """
    returns minimum and maximum values in a sequence
    :param data: iterable sequence
    :return: tuple with minimum and maximum values
    """
    return min(data), max(data)


print(min_max([9,3,45,56,34,78,34,45,23]))
print(min_max({9,3,56,78,34,45,23}))
print(min_max((9,3,56,78,34,45,23)))

print(min_max.__doc__)