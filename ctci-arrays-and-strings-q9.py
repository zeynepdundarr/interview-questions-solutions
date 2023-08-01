# 1.9
# String Rotation; Assume you have a method i s S u b s t r i n g which checks if one word is a substring
# of another. Given two strings, si and s2, write code to check if s2 is a rotation of si using only one
# call to i s S u b s t r i n g [e.g., " w a t e r b o t t l e " is a rotation o P ' e r b o t t l e w a t " ) ,
# Hints: #34, #88,#W4


#88.1,9We are essentially asking if there's a way of splitting the first string into two parts, x and
# y, such that the first string is xy and the second string is yx. For example, x = wat and
# y = e r b o t t l e . The first string is xy = w a t e r b o t t l e . The second string is yx =
# erbottlewat,

# find the first character of s1 in s2
# this is rotation point
# split the line into two by this point

# check if both strings are substrings of s1
# what happens if it is the start of the string is the beginning of the s2

# check first three elements in s1 and use it to find rotation point in s2
def string_rotation(s1, s2):
    # assume that checking 3 elements' equality is enough for recognizing beginning of s1
    initial_slice_s1 = s1[0:3]
    for i in range(len(s2)):
        if i+3 <= len(s2):
            slice_s2 = s2[i:i+3]
            if slice_s2 == initial_slice_s1:
                rotation_point = i
                x = s2[rotation_point:len(s2)]
                y = s2[0:rotation_point]
                return isSubstr(s1, x) and isSubstr(s1, y)
            else:
                continue
    return False

def isSubstr(s2, x):
    substr_arr = [s2[i:j] for i in range(0, len(s2)) for j in range(i+1, len(s2)+1)]
    if x in substr_arr:
        return True
    else:
        return False
        



print(string_rotation("waterbottle", "erbottlewat"))