class Solution(object):
    def repeatedSubstringPattern(self, s):
        double =s+s
        return s in double[1:-1]