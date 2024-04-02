class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:      
        if s1 == s2:
            return True
        
        diff_ind = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_ind.append(i)
                
        if len(diff_ind) != 2:
            return False
                        
                
                
        return s1[diff_ind[0]] == s2[diff_ind[1]] and s1[diff_ind[1]] == s2[diff_ind[0]]
            
                
                
        
        