class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x , y = 0 , 0
        visited.add((x , y))
        
        for direction in path:
            if direction == 'N':
                y+=1
            if direction == 'E':
                x+=1
            if direction == 'S':
                y -=1
            if direction == 'W':
                x-=1
                
            if (x , y) in visited:
                return True
            visited.add((x , y))
            
        return False
            

                
            
        