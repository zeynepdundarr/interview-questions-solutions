# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #117, #132

unique_dict = {}

def is_unique(str_a):
    for curr_ch_index in range(len(str_a)):
        for ch_index in range(curr_ch_index+1, len(str_a)):
            if ord(str_a[ch_index]) - ord(str_a[curr_ch_index]) == 0:
                return False
            else:
                continue
                
    return True


# no additional data structures?
# abca should fail the test
# abca 
# subtract each character from each character if there is zeros, return fail
print(is_unique("abca"))