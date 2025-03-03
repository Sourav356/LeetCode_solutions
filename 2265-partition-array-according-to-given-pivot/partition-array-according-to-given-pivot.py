class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greter = []
        pivotl = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                greter.append(nums[i])
            elif nums[i] == pivot:
                pivotl.append(nums[i])

        mainlist = less + pivotl + greter
        return mainlist
        