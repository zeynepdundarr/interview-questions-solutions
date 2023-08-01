# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale,pie
# -> true
# pales,pale
# -> true
# pale,bale -> true
# pale,bake -> false
# Hints: #23, #97, it 130

# delete
# insert
# replace

# pie -> pale

# 2 chars in common
# len(b) - len(a)

# add and replace


def one_away(a, b):
    
    # sorted maybe unnecessary
    a = list("".join(sorted(a)))
    b = list("".join(sorted(b)))

    # deletion
    result_list = list(filter(lambda x: x not in b, a))
    if len(result_list) == 1:
            return True
    return False


print(one_away("pale","bake"))
