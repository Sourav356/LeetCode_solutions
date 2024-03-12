class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
        app = []
        for num, count in dic.items():
            if count == 1:
                app.append(num)

        return app
        