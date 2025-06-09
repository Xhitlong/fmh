class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[1]
        p1=0
        p2=0
        p3=0
        for i in range(1,n):
            num=min(nums[p1]*2,min(nums[p2]*3,nums[p3]*5))
            if (num==nums[p1]*2):
                p1+=1
            if (num==nums[p2]*3):
                p2+=1
            if (num==nums[p3]*5):
                p3+=1
            nums.append(num)
        return nums[-1]