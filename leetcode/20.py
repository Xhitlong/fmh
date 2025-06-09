class Solution(object):
    def isValid(self, s):
        while True:
            temp = s.replace('()', '').replace('[]', '').replace('{}', '')
            if temp == '':
                return True
            elif temp == s:
                return False
            else:
                s = temp