# Author: Mahtab Zilaie
# Date: November 19 2019
# Description: function takes a string parameter and returns
## how many of each letter is in a string.

def count_letters(s):
    """takes string parameter and counts/returns amount
    of each letter in that string(only letters)"""
    new_dict = dict()
    for x in s.upper():
        if x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if x in new_dict:
                new_dict[x] += 1
            else:
                new_dict[x] = 1
    return new_dict
