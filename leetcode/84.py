class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        stack = [-1]
        ans = 0
        for i in range(n):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                higher = stack.pop()  
                ans = max(ans, heights[higher]*(i-stack[-1]-1))
            stack.append(i)
        for i in range(len(stack)-1): # 注意还有哨兵的存在
            ans = max(ans, heights[stack.pop()]*(n-stack[-1]-1))
        return ans