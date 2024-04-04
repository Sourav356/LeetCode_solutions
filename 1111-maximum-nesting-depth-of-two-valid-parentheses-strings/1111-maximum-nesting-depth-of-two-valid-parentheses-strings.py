class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth = 0
        result = []
        
        for char in seq:
            if char == '(':
                depth+=1
                result.append(depth % 2)
            elif char== ')':
                result.append(depth % 2)
                depth-=1
                
        return result
        