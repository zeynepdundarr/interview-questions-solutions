# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def rotate_matrix(matrix):
    N = len(matrix)

    new_matrix = [[0] * N ] * N

    for i in range(N):
        for k in range(N):
            new_matrix[i][N-1-k] = matrix[k][i]
    return new_matrix

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]] 

# print(rotate_matrix(matrix))



def rotate_matrix_2(matrix):
    N = len(matrix)

    rows, cols = (N, N)
    new_matrix = [[0 for i in range(cols)] for j in range(rows)]   

    for i in range(N):
        for k in range(N):
            new_matrix[i][N-1-k] = matrix[k][i]
    return new_matrix

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]] 

print(rotate_matrix_2(matrix))