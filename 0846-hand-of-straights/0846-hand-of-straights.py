from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
    
    # Count the occurrences of each card
        card_count = Counter(hand)
    
    # Create a min-heap from the unique card values
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
    
        while min_heap:
        # Get the smallest card
            first = min_heap[0]
        
        # Attempt to form a group starting with this card
            for i in range(groupSize):
                card = first + i
                if card_count[card] == 0:
                    return False
                card_count[card] -= 1
            
            # If the count becomes zero, remove it from the heap
                if card_count[card] == 0:
                    if card != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
    
        return True
        

        