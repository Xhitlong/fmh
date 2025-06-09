class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(i,course,flag,res):
            if flag[i] == 0:
                return False
            elif flag[i] == 1:
                return True
            else:
                flag[i] = 0
                for j in range(len(course[i])):
                    if not dfs(course[i][j],course,flag,res):
                        return False
                flag[i] = 1
                res.append(i)
                return True

        flag = [-1]*numCourses
        course = [[] for i in range(numCourses)]
        res = []
        for i in range(len(prerequisites)):
            course[prerequisites[i][0]].append(prerequisites[i][1])
        for i in range(numCourses):
            if not dfs(i,course,flag,res):
                res = []
                break
        return res
