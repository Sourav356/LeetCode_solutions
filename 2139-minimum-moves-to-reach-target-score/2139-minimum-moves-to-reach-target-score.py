class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //=2
                maxDoubles -=1
            elif target % 2 == 1:
                target -=1
            else:
                move+= target - 1
                
                break
            move+=1
                
        return move