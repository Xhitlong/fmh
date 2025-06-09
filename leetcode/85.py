class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        dp_top = [[0]*(n+1) for _ in range(m+1)]
        dp_left = [[0]*(n+1) for _ in range(m+1)]

        maxArea = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == "1":
                    dp_top[i][j] = dp_top[i-1][j]+1
                    dp_left[i][j] = dp_left[i][j-1]+1

                    minHeight = dp_top[i][j]
                    for k in range(j, j-dp_left[i][j], -1):
                        width = j-k+1
                        minHeight = min(minHeight, dp_top[i][k])
                        maxArea = max(maxArea, minHeight*width)

        return maxArea