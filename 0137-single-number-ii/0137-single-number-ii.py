class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
        app = 0
        for num, count in dic.items():
            if count == 1:
                app+=num
                break 
        return app
        