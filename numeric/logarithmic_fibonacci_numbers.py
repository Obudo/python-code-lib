def mat_prod(mat1, mat2):
    result = [[0 for _ in mat2[0]] for _ in mat1]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

def matrix_pow(mat, n):
    retval = [[1, 0], [0, 1]]
    i = 1
    while i <= n:
        if i & n:
            retval = mat_prod(retval, mat)
        i <<= 1
        mat = mat_prod(mat, mat)
    return retval

def get_fibonacci_number(n):
    initial_matrix = [[1, 1], [1, 0]]
    nth_power_matrix = matrix_pow(initial_matrix, n)
    return nth_power_matrix[1][0]


if __name__ == '__main__':
    for i in range(50):
        print(get_fibonacci_number(i))