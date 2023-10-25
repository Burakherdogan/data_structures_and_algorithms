class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()                   #O(1)
        count = 0                       #O(1)
        for i in range(len(s)):         #O(n)
            if s[i] == " ":
                count = 0
            else:
                count += 1
        return count


#Total O(n)