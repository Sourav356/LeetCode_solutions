class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait = [0]*len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                wait[idx] = i-idx
                
            stack.append(i)
        return wait
        