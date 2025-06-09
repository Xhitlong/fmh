class Solution(object):
    def networkDelayTime(self, times, n, k):
        def dij(graph,node,n):
            q = []
            dis = [float('inf')] * n
            dis[node] = 0
            heapq.heappush(q,(0,node))
            while q:
                dx,index = heapq.heappop(q)
                if dx > dis[index]:
                    continue
                for i,a in graph[index]:
                    newdis = dis[index] + a
                    if newdis < dis[i]:
                        dis[i] = newdis
                        heapq.heappush(q,(dis[i],i))
            return dis
        graph = [[] for _ in range(n)]
        for i in times:
            graph[i[0]-1].append([i[1]-1,i[2]])
        dis = dij(graph,k-1,n)
        if max(dis) == float('inf'):
            return -1
        return max(dis)