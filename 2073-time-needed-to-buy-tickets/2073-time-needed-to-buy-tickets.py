from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i, num_tic in enumerate(tickets):
            queue.append((i, num_tic))
            
        time_taken = 0
        curr_time = 0
        
        while queue:
            curr_time +=1
            person_index, num_tic = queue.popleft()
            if num_tic > 0:
                num_tic -=1
                if num_tic == 0:
                    if person_index == k:
                        return time_taken + 1
                else:
                    queue.append((person_index,num_tic))
            time_taken +=1
            
        return -1
                    
                    
            
                