class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0  # Pointer for the heaviest person
        right = len(people) - 1  # Pointer for the lightest person
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Move to the next heaviest person
            right -= 1  # Move to the next lightest person
            boats += 1  # Increment the number of boats used
        
        return boats
        