class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [False]*n
        visited = [False]*n
        def traverse(node, color):
            if not visited[node]:
                visited[node] = True
                colors[node] = color
            for nei in graph[node]:
                if not visited[nei]:
                    traverse(nei, 1-color)
                elif colors[nei] == color:
                    return False
            return True
        for i in range(n):
            if colors[i] == False:
                color = 0 
            else:
                color = colors[i]
            if not traverse(i,color):
                return False
        return True