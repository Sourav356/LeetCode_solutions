class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        citations.sort(reverse=True)
        
        for i, citation in enumerate (citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break 
                
        return h
            
        