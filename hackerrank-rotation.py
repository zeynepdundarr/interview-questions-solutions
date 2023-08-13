def rotate_array(arr, d):

    new_arr = [['x'] for i in range(len(arr))]

    for i in range(len(arr)):
        val = i - d
        if i - d >= 0:
            shifted_index = i-d
        else:
            shifted_index = len(arr) - d + i

        new_arr[shifted_index] = arr[i]
        print(shifted_index)
 
    return new_arr



n = 5
d = 4


arr = [1,2,3,4,5]

print(rotate_array(arr, d))