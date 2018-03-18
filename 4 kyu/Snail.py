# Snail Sort
# Given an n x n array, return the array elements arranged from outermost
# elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array
# consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:
#
#
#
# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as [[]]

def snail(array):
    f = []
    while array:
        print(array)
        f.extend(array.pop(0))
        if not array:
            continue
        for i in array:
            f.append(i.pop(-1))
        if not array:
            continue
        f.extend(array.pop(-1)[::-1])
        if len(array) > 1:
            l = []
            for i in array:
                l.append(i.pop(0))
            f.extend(l[::-1])
    return f