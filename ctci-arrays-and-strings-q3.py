# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input:" M r 3ohn S m i t h    " 23
# Output:"Mr%203ohn%20Smith"
# Hints: #53,0118

# append percentage to before substr
# append remaining to after substr

# str_a[0,i+1] += "%20"


def replace_spaces(str_a):
    size = len(str_a)
    i = 0
    while i != size:
        if str_a[i] == " ":
            remaining = str_a[i+1:len(str_a)]
            str_a = str_a[0:i] + "%20"
            str_a = str_a + remaining
            i += 3
            size += 2
        else:
            i += 1
    return str_a



print(replace_spaces(" M r 3ohn S m i t h    "))


" M r"
"%20M r"
"%20M%20r"
" M r"

" M%20" + "r"




