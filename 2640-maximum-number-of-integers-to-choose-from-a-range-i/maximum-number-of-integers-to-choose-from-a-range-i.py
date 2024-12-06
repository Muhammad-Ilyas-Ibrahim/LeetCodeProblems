class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        total = 0
        count = 0
        banned_set = set(banned)  # Use a set for O(1) lookup

        # Iterate through numbers from 1 to n
        for value in range(1, n + 1):
            if value in banned_set:  # Skip banned values
                continue
            if total + value > maxSum:  # Stop if sum exceeds maxSum
                break
            total += value  # Add value to total
            count += 1  # Increment count of valid numbers

        return count
