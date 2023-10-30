class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if x < INT_MAX and x> INT_MIN:
            x = str(x)
            if x[0]!='-':
                x = x[::-1]
            else:
                x = '-'+x[:0:-1] 
        x = int(x)
        if x < INT_MAX and x > INT_MIN:
            return x
        return 0