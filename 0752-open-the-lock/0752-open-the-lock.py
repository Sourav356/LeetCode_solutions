class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        
        queue = deque([('0000', 0)])
        visited = set(['0000'])
        
        while queue:
            current, moves = queue.popleft()
            if current == target:
                return moves
            
            for i in range(4):
                for j in [-1, 1]:
                    new_wheel = current[:i] + str((int(current[i]) + j) % 10) + current[i+1:]
                    if new_wheel not in deadends and new_wheel not in visited:
                        visited.add(new_wheel)
                        queue.append((new_wheel, moves + 1))
        
        return -1
        