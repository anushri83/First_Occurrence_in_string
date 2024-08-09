class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(needle)
        for i in range(0,m):
            if haystack[0:m]==needle:
                return 0
            else:
                return -1
