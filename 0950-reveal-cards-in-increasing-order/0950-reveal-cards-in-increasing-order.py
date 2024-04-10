from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        indices = deque(range(n))
        new_deck = [0] * n

        for card in deck:
            new_deck[indices.popleft()] = card
            if indices:
                indices.append(indices.popleft())
                
        return new_deck