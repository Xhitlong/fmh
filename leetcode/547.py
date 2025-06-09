class Solution(object):
  def findCircleNum(self, isConnected):
      """
      无向图的连通数
      :type isConnected: List[List[int]]
      :rtype: int
      """
      # 用栈实现广度优先遍历
      stack = []
      M = len(isConnected)        # 顶点数
      v = [1 for _ in range(M)]   # 顶点的标记数组，0就是访问过了
      count = 0
      search_list = []
      while sum(v) > 0:
          # idx: 当前准备搜索的节点
          idx = 0
          while v[idx] == 0:
              idx += 1
          # 到这里就找到了当前第一个还没有访问过的节点idx
          # 准备从idx开始搜索第一个图，count可以直接加一
          search_list.append([])
          count += 1

          # 剪枝，如果只剩下一个节点那么直接退出
          if sum(v) == 1:
              v[idx] = 0
              search_list[-1].append(idx)
              break
          # 把节点压入栈中，准备找他的邻接点
          stack.append(idx)
          while len(stack) > 0:
              # 拿出最底下的节点，找他的邻接点
              idx2 = stack.pop(0)
              # 用search_list记录连通图，也就是BFS的路径
              search_list[-1].append(idx2)

              v[idx2] = 0
              # 如果节点未被访问并且是当前节点的邻接点，那么压栈，表示还可以接着往下走
              for idx3,i in enumerate(isConnected[idx2]):
                  if i == 1 and v[idx3] == 1:
                      stack.append(idx3)
      # print(search_list)
      return count