class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for index, n in enumerate(nums):
            if n >= target:
                return index
        
        return len(nums)

