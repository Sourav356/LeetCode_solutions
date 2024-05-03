class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        part1 = list(map(int, version1.split(".")))
        part2 = list(map(int, version2.split(".")))
        
        max_len = max(len(part1), len(part2))
        part1 += [0]* (max_len - len(part1))
        part2 += [0] * (max_len - len(part2))
                       
        for i in range(max_len):
            if part1[i] < part2[i]:
                return -1
                break
            elif part1[i] > part2[i]:
                return 1
                break
        else:
            return 0
        
        
        
                    
                       