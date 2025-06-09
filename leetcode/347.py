class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 解法2
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        import heapq
        res = heapq.nlargest(k, table, key=lambda kk: table[kk])
        return res

    def otherSolution(self, nums, k):
        # 解法1
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        sorted_li = sorted(table.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_li[i][0])

        return res

        # 解法3
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        import heapq
        res = []
        for key, value in table.items():
            heapq.heappush(res, [value, key])
        for i in range(len(res)-k):
            heapq.heappop(res)

        return [item[1] for item in res]

        # 解法3 改进1
        table = {}
        for num in nums:
            if num in table: table[num] += 1
            else: table[num] = 1

        import heapq
        res = []
        for key, value in table.items():
            if len(res) < k:
                heapq.heappush(res, [value, key])
            else:
                heapq.heappushpop(res, [value, key])


        return [item[1] for item in res]