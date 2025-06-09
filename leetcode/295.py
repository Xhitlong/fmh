class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.data.append(num)
        
    def findMedian(self):
        """
        :rtype: float
        """
        ldata = len(self.data)
        self.data.sort()
        if ldata%2 == 1:
            return self.data[ldata/2]
        else:
            return float(self.data[ldata/2]+self.data[ldata/2-1])/2