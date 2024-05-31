class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #This the normal approach where it doesnot follow this condition You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
#         dic = {}
#         for num in nums:
#             dic[num] = dic.get(num,0)+1
#         app = []
#         for num, count in dic.items():
#             if count == 1:
#                 app.append(num)

#         return app
    
    # The actual approach is 
        xor_all = 0
        for num in nums:
            xor_all ^= num
            
        diff_bit = xor_all & (-xor_all)
        
        unique1 = 0
        unique2 = 0
        
        for num in nums:
            if num & diff_bit:
                unique1 ^=num
            else:
                unique2 ^=num
        return [unique1, unique2]
        