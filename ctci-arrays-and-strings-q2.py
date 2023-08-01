# check 

# 1.2
# Check Permutation: Given two strings, write a mis ethod to decide if one is a permutation of the
# other.
# Hints: f t , #84, #122, #131

# check is permutation
# sort the string and substract

def is_permutation(str_1: str, str_2: str):
    
    str_1_sorted = ''.join(sorted(str_1))
    str_2_sorted = ''.join(sorted(str_2))

    for i in range(len(str_1_sorted)):
        if ord(str_1_sorted[i]) - ord(str_2_sorted[i]) != 0:
            return False
    return True


print(is_permutation("zeynep", "egynepz"))