from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        # 记录任意两点之间的距离
        equations_dic = defaultdict(dict)
        for i in range(len(values)):
            x, y = equations[i]
            equations_dic[x][x] = equations_dic[y][y] = 1
            equations_dic[x][y] = values[i]
            equations_dic[y][x] = 1 / values[i]
        all_chrs = equations_dic.keys()
        for b in all_chrs:
            for a in all_chrs:
                for c in all_chrs:
                    if c not in equations_dic[a]:
                        num1, num2 = equations_dic[a].get(b), equations_dic[b].get(c)
                        if num1 and num2:
                            equations_dic[a][c] = num1 * num2

        return [equations_dic[x].get(y, -1) for x, y in queries]