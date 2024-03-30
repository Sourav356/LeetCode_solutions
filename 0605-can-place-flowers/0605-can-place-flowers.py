class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        for i in range(len(flowerbed)):
    # Check if the current plot and its adjacent plot are both empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
        # Plant a flower in the current plot
                flowerbed[i] = 1
        # Decrease the count of remaining flowers to plant
                planted +=1
        # If all flowers are planted, return True
                if planted == n:
                    return True

        return planted >= n
        