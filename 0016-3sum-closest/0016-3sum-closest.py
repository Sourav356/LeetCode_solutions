class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        for tp in range(len(nums) -2):
            fp , sp =tp +1 , len(nums) -1
            while fp < sp:
                current_sum = nums[fp] + nums[sp] + nums[tp]
                current_diff = abs(current_sum - target)
                if current_diff < abs(closest_sum - target):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    fp +=1
                elif current_sum > target:
                    sp -=1
                else:
                    return current_sum 
                
        return closest_sum 

        
        
        
        