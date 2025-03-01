class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        def placetheZeros(num):
            left = 0
            for right in range(len(num)):
                if num[right]!= 0:
                    num[left],num[right] = num[right],num[left]
                    left +=1
            return num
            

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        zeros = placetheZeros(nums)
        return zeros
                



            
        
        