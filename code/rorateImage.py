class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)-1
        length=0
        if len(matrix)%2==0:
            length=len(matrix)/2
        else:
            length=len(matrix)/2+1
        for i in range(length):
            for j in range(i,len(matrix)-1-i):
                tmp1=matrix[i][j]
                tmp2=matrix[j][n-i]
                tmp3=matrix[n-i][n-j]
                matrix[i][j]=matrix[n-j][i]
                matrix[j][n-i]=tmp1
                matrix[n-i][n-j]=tmp2
                matrix[n-j][i]=tmp3