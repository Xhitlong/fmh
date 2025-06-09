class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 先以 / 为分割符，将字符串分割成许多个字符串（文件名），遍历这些字符串，
        # 如果是正常的文件名就直接入栈，如果是".."弹出栈顶元素，
        # 如果是'.'不用管他，到最后再遍历栈，将出栈的元素插入到返回字符串的头上同时加上'/'。

        #   ../   返回上一级目录
        #   ./   当前的目录
        #   //   视为一个 /
        #    /   在结尾
        stack = []
        for i in path.split('/'):
            if i not in ['', '.', '..']:
                stack.append(i)
            elif i == '..' and stack:
                stack.pop()
        return "/" + "/".join(stack)