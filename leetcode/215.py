class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapsize = len(nums)

        def heapify(nums, index, heapsize):
            max = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < heapsize and nums[left] > nums[max]:
                max = left
            if right < heapsize and nums[right] > nums[max]:
                max = right
            if max != index:
                swap(nums, index, max)
                heapify(nums, max, heapsize)

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def buildHeap(nums, heapsize):
            for i in xrange(heapsize / 2 - 1, -1, -1):
                heapify(nums, i, heapsize)

        buildHeap(nums, heapsize)
        for i in range(k-1):
            swap(nums, 0, heapsize-1)
            heapsize -= 1
            heapify(nums, 0, heapsize)
        return nums[0]