class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        dif = len(nums)
        i = -1

        for index, n in enumerate(nums):
            if target == n:
                return index
            if (n - target) <= dif and (n-target) >= 1:
                dif = n-target
                i = index
                print(f"n={n} | target={target} | i={i}")
        
        if i >= 0:
            return i
        else:
            return len(nums)

