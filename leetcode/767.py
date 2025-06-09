class Solution(object):
    def reorganizeString(self, s):
        from collections import Counter

        counter = Counter(s)  # 统计字符串中每个字符的频率
        max_freq = max(counter.values())  # 找出频率最高的字符的频率
        if max_freq > (len(s) + 1) // 2:  # 如果任何字符的频率大于字符串长度的一半，则无法重新排列
            return ""

        result = [None] * len(s)  # 初始化结果列表
        even_idx, odd_idx = 0, 1  # 初始化偶数索引和奇数索引
        for char, freq in counter.items():  # 遍历每个字符及其频率
            while freq > 0 and freq < len(s) // 2 + 1 and odd_idx < len(s):  # 将频率较低的字符放在奇数索引处
                result[odd_idx] = char
                freq -= 1
                odd_idx += 2
            while freq > 0:  # 将剩余的字符放在偶数索引处
                result[even_idx] = char
                freq -= 1
                even_idx += 2

        return ''.join(result)  # 返回重新排列后的字符串