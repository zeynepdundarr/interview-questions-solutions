# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints: #44, #117, #132


#44.1.1Try a hash table.
#117.1.1Could a bit vector be useful?
#132.1.1Can you solve it in 0 ( N l o g N) time? What might a solution like that look like?

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


# You should first ask your interviewer if the string is an ASCII string or a Unicode string. Asking this question
# will show an eye for detail and a solid foundation in computer science. We'll assume for simplicity the char-
# acter set is ASCII. If this assumption is not valid, we would need to increase the storage size.
# One solution is to create an array of boolean values, where the flag at index i indicates whether character
# i in the alphabet is contained in the string. The second time you see this character you can immediately
# return f a l s e .
# We can also immediately return f a l s e if the string length exceeds the number of unique characters in the
# alphabet. After all, you can't form a string of 280 unique characters out of a 128-character alphabet.


