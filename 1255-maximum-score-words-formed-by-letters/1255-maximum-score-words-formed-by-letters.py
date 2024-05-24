from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def get_word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)
        
        def can_form_word(word_count, letters_count):
            for c in word_count:
                if word_count[c] > letters_count.get(c, 0):
                    return False
            return True
        
        def backtrack(index, current_score, letters_count):
            if index == len(words):
                return current_score
            
            max_score = current_score
            word = words[index]
            word_score = word_scores[index]
            word_count = word_counts[index]
            
            # Option 1: Skip the current word
            max_score = max(max_score, backtrack(index + 1, current_score, letters_count))
            
            # Option 2: Use the current word, if possible
            if can_form_word(word_count, letters_count):
                for c in word_count:
                    letters_count[c] -= word_count[c]
                max_score = max(max_score, backtrack(index + 1, current_score + word_score, letters_count))
                for c in word_count:
                    letters_count[c] += word_count[c]
            
            return max_score
        
        # Precompute the scores and letter counts for each word
        word_scores = [get_word_score(word) for word in words]
        word_counts = []
        for word in words:
            count = {}
            for c in word:
                count[c] = count.get(c, 0) + 1
            word_counts.append(count)
        
        # Count the available letters
        letters_count = {}
        for c in letters:
            letters_count[c] = letters_count.get(c, 0) + 1
        
        # Start backtracking
        return backtrack(0, 0, letters_count)
        