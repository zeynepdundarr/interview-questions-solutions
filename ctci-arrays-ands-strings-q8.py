# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
# Hints: #17, #74, #102

import numpy as np

def zero_matrix(matrix):

    # make this operation below for the selected index pairs
    # matrix[i,:] = [0] * len(matrix)
    # matrix[:,i] = [0] * len(matrix)
    
    tuple_list = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
               tuple_list.append((i,j))

    for i,j in tuple_list:
        replace_arr_1 = [0] * len(matrix)
        replace_arr_2= [0] * len(matrix[0])
        matrix[i,:] = np.array(replace_arr_2)
        matrix[:,j] =  np.array(replace_arr_1)

    return matrix


matrix = np.array([[1,2,3,4,6],[1,0,3,4,6],[1,2,3,0,6],[1,0,3,4,6]])
print(zero_matrix(matrix))