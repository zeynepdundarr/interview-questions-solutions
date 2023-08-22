def longest_common_substring(string):
    max_len_array = []
 
    for i in range(len(string)):
        dict_common_numbers = {}
        dict_common_numbers[string[i]] = 1
        max_len = 1
        for k in range(i+1, len(string)):
            if string[k] not in dict_common_numbers.keys():
                dict_common_numbers[string[k]] = 1
                max_len += 1
            else:
                break

        max_len_array.append(max_len)
    
    max_len_array = sorted(max_len_array)
    return max_len_array[len(max_len_array)-1]


print(longest_common_substring("pwwkew"))