# Given an array, find the int that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    num = ''
    for i in seq:
        if seq.count(i) % 2 > 0:
            num = i
    return num