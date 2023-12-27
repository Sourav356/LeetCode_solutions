class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)
        if index != -1:
            return index
        else:
            return -1