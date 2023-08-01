# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:T a c t Coa
# Output:True (permutations:
# Hints: #106,
# 1.5
# "taco cat", "atco eta",
# etc.)
# h 0134, § 136
def palindrome_permutation(str):

    # check if every character occurs twice
    memory = {}
    for i in range(len(str)):
        if str[i] in memory.keys():
            memory[str[i].lower()] += 1
        else:
            memory[str[i].lower()] = 1
    
    count = 0
    for key, val in memory.items():
        if val%2 == 1:
            count += 1
        else:
            continue

    if count == 1 or count == 0:
        return True
    else:
        return False
    

print(palindrome_permutation("Zeyyez"))