


m=[[1,2,3],[4,5,6],[7,8,9]]
def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    matrix.reverse()

    i_max =len(matrix )
    j_max =i_max
    i=0
    j=0
    while i<i_max and j<j_max:
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        j+=1
        if j==j_max+1:
            i+=1
            j=i

if __name__ == '__main__':
    rotate(m)
    print(m)