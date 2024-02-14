class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi = []
        nege = []
        main = []

        for i in range(len(nums)):
            if nums[i] < 0:
                nege.append(nums[i])
            else:
                posi.append(nums[i])
        

        for i in range(len(posi)):
            main.append(posi[i])
            main.append(nege[i])
    
        return main
        