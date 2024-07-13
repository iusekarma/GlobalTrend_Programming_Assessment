def transpose(mat):
    r = len(mat)
    c = len(mat[0])

    t_mat = [[0 for _ in range(r)] for _ in range(c)]

    for i in range(r):
        for j in range(c):
            t_mat[j][i] = mat[i][j]

    return t_mat

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix :")
    print(matrix)
    
    print("/nTransposed Matrix :")
    print(transpose(matrix))
    