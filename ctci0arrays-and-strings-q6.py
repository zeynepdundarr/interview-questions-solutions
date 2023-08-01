# 1.6
# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3 , If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, if 110



# check if next character is a repeating character


def string_compression(str_a):
    i = 0 
    new_str = ''
    while i < len(str_a):
        count = find_repeating_char_count(str_a, i)
        if count:
            new_str = new_str + str_a[i] + str(count)
            i += count
             
    if len(str_a) <= len(new_str):
        return str_a
    else: 
        return new_str
    
def find_repeating_char_count(str_a, curr_char_index):
    count = 1
    curr_char = str_a[curr_char_index]
    curr_char_index += 1
    while curr_char_index < len(str_a) and str_a[curr_char_index] == curr_char:
        curr_char_index += 1
        count += 1
    return count

# how many times does it repeat
# check the original string and compressed string




print(string_compression("aabcccccaaa"))
