class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        x = str(x)
        y =  x[::-1]
        if (y == x):
            return True