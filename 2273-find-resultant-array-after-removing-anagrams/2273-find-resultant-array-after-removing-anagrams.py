class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            element1 = sorted(words[i - 1])
            element2 = sorted(words[i])
            if element1 == element2:
                words.pop(i)
            else:
                i+=1
        return words