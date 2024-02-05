class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_l= []
        index_l = []
        left=0
        for char in s:
            s_l.append(s[left])
            index_l.append(left)
            left+=1

        dic = {}
        for i in range(len(index_l)):
            if s_l[i] in dic:
                dic[s_l[i]] = -1  # Mark repeated characters with -1
            else:
                dic[s_l[i]] = i

# Finding the index of the first non-repeating character
        min_index = float('inf')
        for value in dic.values():
            if value != -1 and value < min_index:
                min_index = value

        if min_index != float('inf'):
            return min_index
        else:
            return -1