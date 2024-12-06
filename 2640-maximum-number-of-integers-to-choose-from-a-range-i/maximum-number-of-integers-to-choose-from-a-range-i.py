class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        total = 0
        count = 0
        banned_set = set(banned) 

        
        for value in range(1, n + 1):
            if value in banned_set:  
                continue
            if total + value > maxSum:
                break
            total += value  
            count += 1  

        return count
