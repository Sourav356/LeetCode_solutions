class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])
    
    # Update the counter with the intersection of counts from subsequent words
        for word in words[1:]:
            word_count = Counter(word)
            common_count &= word_count
    
    # Construct the result list based on the characters and their counts
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
    
        return result
        