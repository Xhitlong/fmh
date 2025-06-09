"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        vis = dict()
        def dfs(node):
            if node is None: return None
            if node.val in vis: return vis[node.val]
            new = Node(node.val)
            new.neighbors = []
            vis[node.val] = new

            for i in node.neighbors:
                new.neighbors.append(dfs(i))
            return new

        return dfs(node)