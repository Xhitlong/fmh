from numpy import inf
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.m = 0
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.m = x
        self.stack.append(x - self.m)
        self.m = min(x, self.m)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] < 0:
            self.m = self.m - self.stack[-1]
        self.stack.pop()
    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] >= 0:
            return self.stack[-1] + self.m
        else:
            return self.m
    def getMin(self):
        """
        :rtype: int
        """
        return self.m