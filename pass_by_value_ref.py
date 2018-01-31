# only reference is swapped; not the data.
# numbers and strings are immutable
def swap_nums(n1, n2):
    n2, n1 = n1, n2
    print(n1, n2)


a = 10
b = 20

swap_nums(a, b)
print(a, b)


# Pass by reference.
# List is mutable
def remove_negative(nums):
    for n in nums:
        if n < 0:
            nums.remove(n)

    return nums


values = [20, -69,-92, 58, 65, -12, 56, 78, -45, -55, 25, 14]
new_values = remove_negative(values);
print(new_values);
print(values) # actual list also gets modified.

values2 = [20, -69,-92, 58, 65, -12, 56, 78, -45, -55, 25, 14]
new_values2 = remove_negative(values2[:]); #passing a copy of the list
print(new_values2);
print(values2)



