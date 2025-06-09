class KthLargest(object):
    def __init__(self, k, nums):
        """
        使用整数 k 和整数流 nums 初始化对象
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        # 设置小顶堆  维护前k大的堆
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap,num)
            if len(self.heap) > k:
                heapq.heappop(self.heap)

    def add(self, val):
        """
        将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素
        :type val: int
        :rtype: int
        """
        # 先推入
        heapq.heappush(self.heap, val)
        # 超过k个推出
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]