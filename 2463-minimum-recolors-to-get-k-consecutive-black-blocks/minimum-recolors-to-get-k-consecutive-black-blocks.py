class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_changes = float('inf')

    # Step 1: Count 'W' in the first window of size k
        current_white = sum(1 for i in range(k) if blocks[i] == 'W')

    # Step 2: Use sliding window to check other k-length segments
        min_changes = current_white  # Initialize with the first window's count

        for i in range(k, n):
            if blocks[i - k] == 'W':  # Outgoing element of window
                current_white -= 1
            if blocks[i] == 'W':  # Incoming element of window
                current_white += 1

        # Update the minimum changes required
            min_changes = min(min_changes, current_white)

        return min_changes
        