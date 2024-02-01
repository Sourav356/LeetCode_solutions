class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        i = 0
        while i < n:
            current_array = [nums[i]]
            j = i+1
            
            while j < n and len(current_array)< 3 and nums[j] - current_array[0] <=k:
                current_array.append(nums[j])
                j+=1
                
            if len(current_array) == 3:
                result.append(current_array)
            
            else:
                return []
            
            i = j
        return result
            
                
        
        