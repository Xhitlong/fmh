class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        if n < 1:
            return
        m = len(matrix[0])

        import heapq
        heap = []
        for i in range(n):
            for j in range(m):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heap[0]